function errorHandler(err, req, res, next) {
    res.status(500).json({
        status: false,
        content: err.message
    })
}

function boonErrorHandler(err, req, res, next) {
    if (err.isBoom) {
        const { output } = err
        res.status(output.statusCode).json(output.payload)
    }
    else {
        next(err)
    }
}
module.exports = { errorHandler, boonErrorHandler }