var express = require('express');
var router = express.Router();
const Staff = require("../controllers/staff")

router.get('/:id',  async (req, res, next) => {
    let staff = await Staff.getStaff(req.params.id)
    res.jsonp(staff)
});

module.exports = router;
