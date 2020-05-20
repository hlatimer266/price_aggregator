var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);

app.use(express.static(__dirname + '/views'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', function(req, res) {

    res.render('aggregator.handlebars')

});

function call_lambda(bucket, lambda_function, handlebars_page, req){
    const accesskey = process.env['AWSAccessKey']
    const secretkey = process.env['AWSSecretKey']

    var AWS = require('aws-sdk');
    AWS.config.update({accessKeyId: accesskey
    , secretAccessKey: secretkey});
    AWS.config.region = "us-east-1"

    var s3 = new AWS.S3();
    var lambda = new AWS.Lambda();
    var options = {
    	Bucket : bucket,
        Key : req.query.parm,
        ResponseContentType : 'application/json'
    }

    s3.getObject(options, function(err,data){
        var s3_response = data.Body.toString()

        var params = {
            FunctionName: lambda_function, /* required */
            Payload: s3_response
        };

        lambda.invoke(params, function(err, data) {
            if (err) console.log(err, err.stack); // an error occurred

            var obj = JSON.parse(data.Payload)
            var context = JSON.parse(obj.body)

            brand_model = req.query.parm.replace(".json","")
            context['product'] = brand_model.replace('/'," - ");
            console.log(context);
    		res.render(handlebars_page, context)
        });

    });
}

app.get('/monitor',function(req, res) {
    console.log(req.query.parm);
    call_lambda('monitors-bb-361', 'scrape_prices_monitors', 'monitor.handlebars', req);
})

app.get('/cell_phone',function(req, res) {
    console.log(req.query.parm);
    call_lambda('phones-bb-361', 'scrape_prices_phones', 'phones.handlebars', req);
})

app.get('/tv',function(req, res) {
    console.log(req.query.parm);
    call_lambda('tvs-bb-361', 'scrape_prices_tvs', 'tv.handlebars', req);
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});