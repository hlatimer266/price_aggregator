var express = require('express');
var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);

app.use(bodyParser.urlencoded({ extended: false }));

app.use(bodyParser.json());

app.get('/', function(req, res) {
    var AWS = require('aws-sdk');
    AWS.config.update({accessKeyId: 'AKIA25CCO4L7FMEMBKWJ'
    , secretAccessKey: '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'});
    AWS.config.region = "us-east-1"

    var lambda = new AWS.Lambda();
    var params = {
    FunctionName: 'scrape_prices_monitors', /* required */
    Payload: '{\
        "url":"https://www.ebay.com/p/568422266", \
        "html_tag": "display-price", \
        "vendor" : "ebay" \
    }',
    };

    lambda.invoke(params, function(err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        else     console.log(data.Payload);           // successful response
        var obj = JSON.parse(data.Payload)
        res.send(obj.body);
    });
    
});


app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});