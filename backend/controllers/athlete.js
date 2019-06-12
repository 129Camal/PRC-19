const axios = require('axios');
const Athlete = module.exports;

normalize = function(response) {
    return response.results.bindings.map(obj =>
        Object.entries(obj)
            .reduce((new_obj, [k,v]) => (new_obj[k] = v.value, new_obj),
                    new Object()));
};

async function execQuery(q){
    try{
        var encoded = encodeURIComponent(q);
        response = await axios.get("http://localhost:7200/repositories/cycling" + '?query=' + encoded);
        return(normalize(response.data));
    }
    catch(error) {
        return('ERRO: ' + error)
    }
}

Athlete.getAthletes = () => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?name ?teamname ?c where {
        ?athlete a :Athlete.
        ?athlete :name ?name.
        ?athlete :hasTeam ?team .
        ?team :name ?teamname .
        ?athlete :country ?c .
    }`;

    return execQuery(query);

};