var express = require('express');
var router = express.Router();
const Team = require("../controllers/team")

const { verifyToken } = require('../config/token');

router.get('/', verifyToken, async (req, res, next) => {
    let team = await Team.getTeams()
    res.jsonp(team)
});

router.get('/:id', verifyToken, async (req, res, next) => {
    let team = await Team.getTeam(req.params.id)
    res.jsonp(team)
});

router.get('/:id/athlete', verifyToken, async (req, res, next) => {
    let team = await Team.getAthletes(req.params.id)
    res.jsonp(team)
});

module.exports = router;
