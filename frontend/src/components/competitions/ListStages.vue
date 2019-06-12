<template>
  <v-flex xs12 md12>
    <v-toolbar>
      <v-toolbar-title>Stages</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-data-table :headers="headers" :items="stages" class="elevation-1">
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
      </template>

      <template slot="items" slot-scope="props">
        <tr @click="rowClicked(props.item)">
          <td class="text-xs-center">{{ props.item.name}}</td>
        </tr>
      </template>
    </v-data-table>
    <br>
    <br>
  </v-flex>
  
</template>

<script>
import axios from "axios";

export default {
  name: "listStages",
  methods: {
    rowClicked(item) {
      this.$router.push("/competitions/" + this.$route.params.id +"/" + item.name);
    }
  },
  data() {
    return {
      stages: [],
      headers: [{ text: "Name", value: "name", align: "center", sortable: false }]
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://192.168.1.83:2019/race/" + this.$route.params.id + "/stages")
        .then(res => {
          this.stages = res.data;
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>