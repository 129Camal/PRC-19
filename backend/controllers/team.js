const axios = require('axios');
const Team = module.exports;

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

Team.getTeams = () => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select * where {
        ?team a :Team.
        ?team :name ?name .
        ?team :continent ?continent.
    }`;

    return execQuery(query);

};

Team.getTeam = (id) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select * where {
        :team_${id} :name ?name .
        :team_${id} :continent ?continent.
        :team_${id} :country ?country.
        :team_${id} :email ?email.
        :team_${id} :teamCategory ?category.
        :team_${id} :website ?website.
        
    }`;

    return execQuery(query);

};

Team.getAthletes = (id) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select * where {
        :team_${id} :hasAthlete ?ath.
        ?ath :name ?name.
        ?ath :country ?country.
    }`;

    return execQuery(query);
}


