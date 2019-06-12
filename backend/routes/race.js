var express = require('express');
var router = express.Router();
const Race = require("../controllers/race")

/* GET home page. */
router.get('/all',  async (req, res, next) => {
    let races = await Race.listRaces()
    res.jsonp(races)
});

router.get('/:id/stages',  async (req, res, next) => {
    let races = await Race.listStages(req.params.id)
    res.jsonp(races)
});

router.get('/:id/stage/:stage',  async (req, res, next) => {
    let races = await Race.getStageResult(req.params.id, req.params.stage)
    res.jsonp(races)
});

router.get('/general/:name',  async (req, res, next) => {
    let race = await Race.getGeneral(req.params.name)
    res.jsonp(race)
});

router.get('/points/:name',  async (req, res, next) => {
    let race = await Race.getPoints(req.params.name)
    res.jsonp(race)
});

router.get('/mountain/:name',  async (req, res, next) => {
    let race = await Race.getMountain(req.params.name)
    res.jsonp(race)
});

router.get('/youth/:name',  async (req, res, next) => {
    let race = await Race.getYouth(req.params.name)
    res.jsonp(race)
});

module.exports = router;
