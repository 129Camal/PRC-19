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

    select ?athlete ?name ?teamname ?c where {
        ?athlete a :Athlete.
        ?athlete :name ?name.
        ?athlete :hasTeam ?team .
        ?team :name ?teamname .
        ?athlete :country ?c .
    }`;

    return execQuery(query);

};

Athlete.getAthlete = (id) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select * where {
        :athlete_${id} :name ?name.
        :athlete_${id} :hasTeam ?team.
        ?team :name ?teamname.
        :athlete_${id} :birthdate ?birth.
        :athlete_${id} :country ?country.
    
    
    }`;

    return execQuery(query);

};

Athlete.getAthleteClassification = (name) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?rank ?tour where {
        ?s a :Race.
        ?s :hasGeneral ?general .
        ?s :name ?tour .
        ?general :hasPosition ?positions .
        ?positions :rank ?rank .
        ?positions :name "${name}" .
        
    }`;

    return execQuery(query);

};

