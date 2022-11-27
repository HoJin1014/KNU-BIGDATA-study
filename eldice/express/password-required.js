module.exports = (req, res, next) => {
    const author = req.get("author");
    
    if (!author) {
        next(new Error("No Author"));
        return;
    }
    
    // admin 확인하기
    if (author == 'admin') {
        const password = req.get('password');
        if (password !== '12345678') {
            next(new Error('NotAuthorized'));
            return
        }
    }
    next();
}