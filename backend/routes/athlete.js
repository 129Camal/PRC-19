var express = require('express');
var router = express.Router();
const Race = require("../controllers/athlete")

router.get('/',  async (req, res, next) => {
    let race = await Race.getAthletes(req.params.name)
    res.jsonp(race)
});

module.exports = router;
