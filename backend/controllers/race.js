const axios = require('axios');
const Race = module.exports;

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

Race.listRaces = async () => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?names ?country ?date ?class where {
        ?races a :Race.
        ?races :name ?names.
        ?races :class ?class.
        ?races :country ?country.
        ?races :date ?date.
    }`;

    var res = await execQuery(query);
    return res;
};

Race.getGeneral = (name) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?rank ?name ?team ?value where {
        ?s a :Race.
        ?s :name "${name}" .
        ?s :hasGeneral ?general .
        ?general :hasPosition ?positions .
        ?positions :rank ?rank .
        ?positions :name ?name .
        ?positions :team ?team .
        ?positions :value ?value .
        
    }`;

    return execQuery(query);
};

Race.getPoints = (name) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?rank ?name ?team ?value where {
        ?s a :Race.
        ?s :name "${name}" .
        ?s :hasPoints ?general .
        ?general :hasPosition ?positions .
        ?positions :rank ?rank .
        ?positions :name ?name .
        ?positions :team ?team .
        ?positions :value ?value .
        
    }`;

    return execQuery(query);
};

Race.getMountain = (name) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?rank ?name ?team ?value where {
        ?s a :Race.
        ?s :name "${name}" .
        ?s :hasMountain ?general .
        ?general :hasPosition ?positions .
        ?positions :rank ?rank .
        ?positions :name ?name .
        ?positions :team ?team .
        ?positions :value ?value .
        
    }`;

    return execQuery(query);
};

Race.getYouth = (name) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?rank ?name ?team ?value where {
        ?s a :Race.
        ?s :name "${name}" .
        ?s :hasYouth ?general .
        ?general :hasPosition ?positions .
        ?positions :rank ?rank .
        ?positions :name ?name .
        ?positions :team ?team .
        ?positions :value ?value .
        
    }`;

    return execQuery(query);
};

Race.listStages = (id) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?stages ?name where {
        ?races a :Race.
        ?races :name "${id}".
        ?races :hasStage ?stages.
        ?stages :name ?name.
    }`;

    return execQuery(query);
};

Race.getStageResult = (id, stage) => {
    const query = `PREFIX : <http://www.semanticweb.org/fredericopinto/ontologies/2019/5/cyclingworld#>

    select ?rank ?name ?team ?value where {
        ?races a :Race.
        ?races :name "${id}".
        ?races :hasStage ?stages.
         ?stages :name "${stage}".
        ?stages :hasClassification ?class.
        ?class :hasPosition ?positions.
        ?positions :rank ?rank.
        ?positions :name ?name.
        ?positions :team ?team.
        ?positions :value ?value.
    }`;

    return execQuery(query);
};