const MysqlLib = require('../lib/mysql')
const bcrypt = require('bcrypt')

class UsuarioService {

    constructor() {
        this.db = new MysqlLib()
    }

    async getLast() {
        const sql = `select usuario_id as id,
                    usuario_nombre as usuario 
                    from tbl_usuario 
                    order by usuario_id desc limit 1`
        const result = await this.db.query(sqlLast, [])
        return result
    }
    async create(usuario) {
        const passwordEncriptado = await bcrypt.hash(usuario.password, 10)
        const sqlcreate = `insert into tbl_usuario(usuario_nombre,usuario_password)
                            values(?,?)`

        await this.db.query(sqlcreate, [usuario.usuario, passwordEncriptado])
        const result = await this.db.getLast()
        return result
    }
}

module.exports = UsuarioService