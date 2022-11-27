const express = require('express');

// 라우터
const notesRouter = require('./routes/notes');
const usersRouter = require('./routes/users');

// 미들웨어
const logger = require('./middlewares/request-logger'); // 로거
const error404 = require('./middlewares/not-found'); // 404 error
const error500 = require('./middlewares/error-handler'); // 500 error(서버에러)
const auth = require('./middlewares/password-required'); // 인증

const app =express();

app.use(logger);
app.use(error404);
app.use(error500);
app.use('/notes', notesRouter);
app.use('/users', auth , usersRouter);

app.listen(8080, () => {
	console.log('SERVER STARTED');
});