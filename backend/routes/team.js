var express = require('express');
var router = express.Router();
const Team = require("../controllers/team")

router.get('/',  async (req, res, next) => {
    let team = await Team.getTeams()
    res.jsonp(team)
});

router.get('/:id',  async (req, res, next) => {
    let team = await Team.getTeam(req.params.id)
    res.jsonp(team)
});

router.get('/:id/athlete',  async (req, res, next) => {
    let team = await Team.getAthletes(req.params.id)
    res.jsonp(team)
});

module.exports = router;
