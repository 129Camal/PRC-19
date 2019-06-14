<template>
  <v-flex xs12 md12>
    <v-toolbar color="grey lighten-2">
      <v-toolbar-title>Athlete Classifications</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-data-table :headers="headers" :items="classification" class="elevation-1">
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
      </template>

      <template slot="items" slot-scope="props">
        <tr @click="rowClicked(props.item)">
          <td class="text-xs-center">{{ props.item.rank}}</td>
          <td class="text-xs-center">{{ props.item.tour}}</td>
        </tr>
      </template>
    </v-data-table>
  </v-flex>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "listClassification",
  props: ["athName"],
  computed: mapGetters(["getToken"]),
  methods: {
    rowClicked(item) {
      this.$router.push("/competitions/" + item.tour);
    }
  },
  data() {
    return {
      classification: [],
      headers: [
        { text: "Rank", value: "rank", align: "center" },
        { text: "Race", value: "tour", align: "center", sortable: false }
      ]
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://localhost:2019/athlete/" + this.$route.params.id + "/" + this.athName,  {
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