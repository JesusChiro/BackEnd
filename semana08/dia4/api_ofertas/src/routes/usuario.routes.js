const express = require('express')
const UsuarioService = require('../services/usuario.service')

const boom = require('@hapi/boom')

function usuarioApi(app) {
    const router = express.Router()
    app.use('/usuario', router)

    const objUsuario = new UsuarioService()

    router.post('/', async function (req, res) {
        const { body: usuario } = req
        const authUsuario = await objUsuario.authenticate({ usuario })
        if (authUsuario.id > 0) {
            const token = jwt.sign(
                authUsuario,
                config.jwt_secret,
                {
                    expiresIn: '1h'
                }
            )
            res.status(200).json({
                status: true,
                content: token
            })
        } else {
            res.status(401).json({
                status: false,
                content: 'datos invalidos'
            })
        }
    })
}

module.exports = usuarioApi