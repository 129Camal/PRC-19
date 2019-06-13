var express = require('express');
var router = express.Router();
const Athlete = require("../controllers/athlete")

router.get('/',  async (req, res, next) => {
    let ath = await Athlete.getAthletes(req.params.name)
    res.jsonp(ath)
});

router.get('/:id',  async (req, res, next) => {
    let ath = await Athlete.getAthlete(req.params.id)
    res.jsonp(ath)
});

router.get('/:id/:nome',  async (req, res, next) => {
    let classi = await Athlete.getAthleteClassification(req.params.nome)
    res.jsonp(classi)
});

module.exports = router;
