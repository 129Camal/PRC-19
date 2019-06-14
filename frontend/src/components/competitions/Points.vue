<template>
  <v-container grid-list-xs v-if="classification[0]">
    <v-toolbar color="green lighten-2">
      <v-toolbar-title>Points Classification</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-data-table :headers="headers" :items="classification" class="elevation-1">
      <template v-slot:no-data>
        <v-alert
          :value="true"
          color="error"
          icon="red"
        >Sorry, points classification not available! :(</v-alert>
      </template>

      <template slot="items" slot-scope="props">
        <tr>
          <td class="text-xs-center">{{ props.item.rank }}</td>
          <td class="text-xs-center">{{ props.item.name}}</td>
          <td class="text-xs-center">{{ props.item.team }}</td>
          <td class="text-xs-center">{{ props.item.value}}</td>
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "points",
  computed: mapGetters(["getToken"]),
  data() {
    return {
      classification: [],
      headers: [
        { text: "Position", value: "rank", align: "center" },
        { text: "Name", value: "name", align: "center", sortable: false },
        { text: "Team", value: "team", align: "center", sortable: false },
        { text: "Result", value: "value", align: "center", sortable: false }
      ]
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://localhost:2019/race/points/" + this.$route.params.id, {
          headers: { Authorization: "Bearer " + this.getToken }
        })
        .then(res => {
          this.classification = res.data;
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>