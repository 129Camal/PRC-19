var createError = require('http-errors');
var express = require('express');
var path = require('path');
const cors = require('cors')
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const mongoose = require('mongoose')

var raceRouter = require('./routes/race');
var athleteRouter = require('./routes/athlete');
var teamRouter = require('./routes/team')
var staffRouter = require('./routes/staff')
var userRouter = require('./routes/users')

var app = express();

//Connection to the MongoDB
mongoose.connect('mongodb://127.0.0.1:27017/Cycling', {useNewUrlParser:true})
  .then(()=> console.log("Mongo Connected!"))
  .catch(()=>console.log("Error Connection!"))

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With');
  next();
});

app.use(logger('dev'));
app.use(cors())
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/race', raceRouter)
app.use('/athlete', athleteRouter)
app.use('/team', teamRouter)
app.use('/staff', staffRouter)
app.use('/users', userRouter)

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
