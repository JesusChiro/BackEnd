const mongoose = require('mongoose')
const Schema = mongoose.Schema

const UserSchema = new Schema({
    email: {
        type: String,
        required: true,
        match: /.+\@.+\..+/,
        unique: true
    },
    password: {
        type: String,
        require: true,
        minlenght: 4
    }
}, {
    timestamps: false,
    versionKey: false
})

module.exports = mongoose.model('users', UserSchema)