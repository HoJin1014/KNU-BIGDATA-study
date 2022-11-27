module.exports = (err, req, res, next) => {
   res.status(500);
   res.send({error: err.message});
};