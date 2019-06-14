var express = require('express');
var router = express.Router();
const Athlete = require("../controllers/athlete")

const { verifyToken } = require('../config/token');

router.get('/', verifyToken, async (req, res, next) => {
    let ath = await Athlete.getAthletes(req.params.name)
    res.jsonp(ath)
});

router.get('/:id', verifyToken, async (req, res, next) => {
    let ath = await Athlete.getAthlete(req.params.id)
    res.jsonp(ath)
});

router.get('/:id/:nome', verifyToken, async (req, res, next) => {
    let classi = await Athlete.getAthleteClassification(req.params.nome)
    res.jsonp(classi)
});

module.exports = router;
