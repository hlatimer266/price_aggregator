var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);

app.use(express.static(__dirname + '/views'));
app.use(bodyParser.json());

app.get('/', function(req, res) {
    
    res.render('aggregator.handlebars')
    
});

app.get('/monitor',function(req, res) {
    
    const accesskey = process.env['AWSAccessKey']
    const secretkey = process.env['AWSSecretKey']
    
    var AWS = require('aws-sdk');
    AWS.config.update({accessKeyId: accesskey
    , secretAccessKey: secretkey});
    AWS.config.region = "us-east-1"

    var s3 = new AWS.S3();
    var lambda = new AWS.Lambda();
    var options = {
        Bucket : 'monitors-bb-361',
        Key : req.query.parm,
        ResponseContentType : 'application/json'
    }

     s3.getObject(options, function(err,data){
        var s3_response = data.Body.toString()

        var params = {
            FunctionName: 'scrape_prices_monitors', /* required */
            Payload: s3_response
            };
        
            lambda.invoke(params, function(err, data) {
                if (err) console.log(err, err.stack); // an error occurred
                
                var obj = JSON.parse(data.Payload)
                var context = JSON.parse(obj.body)

                brand_model = req.query.parm.replace(".json","")
                context['product'] = brand_model.replace('/'," - ");
        
                res.render('monitor.handlebars',context)
            });
        
    });


})

app.get('/cell_phone',function(req, res) {

    console.log(req.query.parm);
    
    const accesskey = process.env['AWSAccessKey']
    const secretkey = process.env['AWSSecretKey']
    
    var AWS = require('aws-sdk');
    AWS.config.update({accessKeyId: accesskey
    , secretAccessKey: secretkey});
    AWS.config.region = "us-east-1"

    var s3 = new AWS.S3();
    var lambda = new AWS.Lambda();
    var options = {
        Bucket : 'phones-bb-361',
        Key : req.query.parm,
        ResponseContentType : 'application/json'
    }

     s3.getObject(options, function(err,data){
        var s3_response = data.Body.toString()

        var params = {
            FunctionName: 'scrape_prices_phones', /* required */
            Payload: s3_response
            };
        
            lambda.invoke(params, function(err, data) {
                if (err) console.log(err, err.stack); // an error occurred

                var obj = JSON.parse(data.Payload)
                var context = JSON.parse(obj.body)
                brand_model = req.query.parm.replace(".json","")
                context['product'] = brand_model.replace('/'," - ");
        
                res.render('phones.handlebars',context)
            });
        
    });
<<<<<<< HEAD


})

app.get('/laptop',function(req, res) {
=======
})

app.get('/laptop',function(req, res) {

    console.log(req.query.parm);

    const accesskey = process.env['AWSAccessKey']
    const secretkey = process.env['AWSSecretKey']

    var AWS = require('aws-sdk');
    AWS.config.update({accessKeyId: accesskey
    , secretAccessKey: secretkey});
    AWS.config.region = "us-east-1"

    var s3 = new AWS.S3();
    var lambda = new AWS.Lambda();
    var options = {
        Bucket : 'laptops-bb-361',
        Key : req.query.parm,
        ResponseContentType : 'application/json'
    }

     s3.getObject(options, function(err,data){
        var s3_response = data.Body.toString()

        var params = {
            FunctionName: 'laptop_scrape', /* required */
            Payload: s3_response
            };

            lambda.invoke(params, function(err, data) {
                if (err) console.log(err, err.stack); // an error occurred

                var obj = JSON.parse(data.Payload)
                var context = JSON.parse(obj.body)

                brand_model = req.query.parm.replace(".json","")
                context['product'] = brand_model.replace('/'," - ");

                res.render('laptop.handlebars',context)
            });

    });


})

app.get('/tv',function(req, res) {
>>>>>>> fbd997fe7313ea166d5a5e224e6a5efb17e26a00

    console.log(req.query.parm);

    const accesskey = process.env['AWSAccessKey']
    const secretkey = process.env['AWSSecretKey']

    var AWS = require('aws-sdk');
    AWS.config.update({accessKeyId: accesskey
    , secretAccessKey: secretkey});
    AWS.config.region = "us-east-1"

    var s3 = new AWS.S3();
    var lambda = new AWS.Lambda();
    var options = {
<<<<<<< HEAD
        Bucket : 'laptops-bb-361',
=======
        Bucket : 'tvs-bb-361',
>>>>>>> fbd997fe7313ea166d5a5e224e6a5efb17e26a00
        Key : req.query.parm,
        ResponseContentType : 'application/json'
    }

     s3.getObject(options, function(err,data){
        var s3_response = data.Body.toString()

        var params = {
<<<<<<< HEAD
            FunctionName: 'laptop_scrape', /* required */
=======
            FunctionName: 'scrape_prices_tvs', /* required */
>>>>>>> fbd997fe7313ea166d5a5e224e6a5efb17e26a00
            Payload: s3_response
            };

            lambda.invoke(params, function(err, data) {
                if (err) console.log(err, err.stack); // an error occurred

                var obj = JSON.parse(data.Payload)
                var context = JSON.parse(obj.body)

                brand_model = req.query.parm.replace(".json","")
                context['product'] = brand_model.replace('/'," - ");

<<<<<<< HEAD
                res.render('laptop.handlebars',context)
=======
                res.render('tv.handlebars',context)
>>>>>>> fbd997fe7313ea166d5a5e224e6a5efb17e26a00
            });

    });


})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});