const os = require('os');

const procesador = os.arch()
const sistema = os.platform()
const cpu = os.cpus().length
const memoria = os.totalmem()

console.log('procesador: ' + procesador)
console.log('sistema operativo: ' + sistema)
console.log('cpu: ' + cpu)
console.log('Memoria operativo: ' + memoria)
memoria_kb = memoria / 1024
console.log('Memoria RAM en kb: ' + memoria_kb)
memoria_mb = memoria_kb / 1024
console.log('Memoria RAM en mb: ' + memoria_mb)
memoria_gb = memoria_mb / 1024
console.log('Memoria RAM en gb: ' + memoria_gb)

//Crear una promesa que permita calcular la memoria en kb, mb, gb

function calcularMemoria(capacidad, tipo) {
    return new Promise((res, rej) => {
        let memoria_convertida = capacidad / 1024
        console.log('Memoria en ' + tipo + ': ' + memoria_convertida)
        res(memoria_convertida)
    })
}

console.log('===============Memoria con Promesas ========================')
calcularMemoria(os.totalmem(), 'KB')
    .then((kb) => calcularMemoria(kb, 'MB'))
    .then((mb) => calcularMemoria(mb, 'GB'))