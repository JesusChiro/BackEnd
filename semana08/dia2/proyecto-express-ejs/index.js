const express = require('express')
const app = express()

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    let peliculas = [
        {
            titulo: 'Super Mario Bross',
            imagen: 'https://www.universalpictures-latam.com/tl_files/content/movies/super_mario_bros/posters/03.jpg'
        },
        {
            titulo: 'Transformers el despertar de las bestias',
            imagen: 'https://www.infobae.com/new-resizer/P4LoLiDBT9ZcwK8bzA8WP7Y9Vgo=/768x1024/filters:format(webp):quality(85)/cloudfront-us-east-1.images.arcpublishing.com/infobae/FPAVWDUGWBC4HCLQ5QFFPA6VKE.png'
        },
        {
            titulo: 'Flash',
            imagen: 'https://pics.filmaffinity.com/Flash-698849219-large.jpg'
        }
    ]
    context = {
        peliculas: peliculas,
    }
    res.render('index', context)
})

app.listen(5000)
console.log('http://localhost:5000')