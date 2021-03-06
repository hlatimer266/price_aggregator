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

function call_lambda(category, req, res){
    const accesskey = process.env['AWSAccessKey']
    const secretkey = process.env['AWSSecretKey']

    var AWS = require('aws-sdk');
    AWS.config.update({accessKeyId: accesskey
    , secretAccessKey: secretkey});
    AWS.config.region = "us-east-1"

    var s3 = new AWS.S3();
    var lambda = new AWS.Lambda();
    var options = {
    	Bucket : category + "s" + "-bb-361",
        Key : req.query.parm,
        ResponseContentType : 'application/json'
    }

    s3.getObject(options, function(err,data){
        var s3_response = data.Body.toString()

        var params = {
            FunctionName: "scrape_prices_" + category + "s", /* required */
            Payload: s3_response
        };

        lambda.invoke(params, function(err, data) {
            if (err) console.log(err, err.stack); // an error occurred

            var obj = JSON.parse(data.Payload)
            var context = JSON.parse(obj.body)

            brand_model = req.query.parm.replace(".json","")
            context['product'] = brand_model.replace('/'," - ");
            console.log(context);
    		res.render(category + '.handlebars', context)
        });

    });
}

app.get('/monitor',function(req, res) {
    console.log(req.query.parm);
    call_lambda('monitor', req, res);
})

app.get('/cell_phone',function(req, res) {
    console.log(req.query.parm);
    call_lambda( 'phone', req, res);
})

app.get('/tv',function(req, res) {
    console.log(req.query.parm);
    call_lambda('tv', req, res);
})

app.get('/laptop',function(req, res) {
    console.log(req.query.parm);
    call_lambda( 'laptop', req, res);
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
