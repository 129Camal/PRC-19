var express = require('express');
var router = express.Router();
const Staff = require("../controllers/staff")

const { verifyToken } = require('../config/token');

router.get('/:id',  verifyToken, async (req, res, next) => {
    let staff = await Staff.getStaff(req.params.id)
    res.jsonp(staff)
});

module.exports = router;
