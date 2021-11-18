import createError from 'http-errors';
import express from 'express';
import path from 'path';
import cookieSession from 'cookie-session';
import logger from 'morgan';

import router from'./router';
import {HMAC} from "./utils/crypto";

const app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

// adjust CORS policy (DO NOT CHANGE)
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "null");
  res.header("Access-Control-Allow-Credentials", "true");
  next();
});

// set lax cookie policies (DO NOT CHANGE)
app.use(cookieSession({
  name: 'session',
  maxAge: 24 * 60 * 60 * 1000, // 24 hours
  signed: false,
  sameSite: false,
  httpOnly: false,
}));

const SECRET = "AVeryVeryHardPasswordHereWithSomeRandomChars-#@%chiuwxv!`"
app.use((req, res, next) => {
  console.log(req.session)
  const jwt = req.session.jwt
  if (jwt)
    delete req.session['jwt']
  if ((jwt !== HMAC(SECRET, JSON.stringify(req.session || {})))) {
    console.log("Invalid jwt token, resetting tokens")
    req.session = {}
    req.session.loggedIn = false;
    req.session.account = {};
  }
  // res.on('finish', async () => {
    // console.log(req.session)
    // console.log("after");
    // console.log(res.head)
    // console.log(req)
    // req.session.jwt = HMAC(SECRET, JSON.stringify(req.session || {}))
    // console.log("req.session")
    // console.log(req.session)
  // })
  next()
})


// initialize session if necessary
app.use((req, res, next) => {
  if(req.session.loggedIn == undefined) {
    req.session.loggedIn = false;
    req.session.account = {};
  }
  next();
});

app.use(router);

// catch 404 and forward to error handler
app.use((req, res, next) => {
  next(createError(404));
});

// error handler
app.use((err, req, res, next) => {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('pages/error');
});

module.exports = app;
