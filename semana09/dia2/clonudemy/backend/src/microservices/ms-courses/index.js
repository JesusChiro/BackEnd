const express = require('express')
const { config } = require('../../config')
const cors = require('cors')

require('../../libs/mongoose.lib')

const app = express()

app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
    res.json({
        message: 'courses microservices active'
    })
})

app.listen(config.ms_courses.port, function () {
    console.log(`ms courses : http://localhost:${config.ms_courses.port}`)
})