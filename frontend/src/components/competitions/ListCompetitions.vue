<template>
  <v-data-table :headers="headers" :items="competitions" class="elevation-1">
    <template v-slot:no-data>
      <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
    </template>

    <template slot="items" slot-scope="props">
      <tr @click="rowClicked(props.item)">
        <td class="text-xs-center">{{ props.item.date }}</td>
        <td class="text-xs-center">{{ props.item.names}}</td>
        <td class="text-xs-center">{{ props.item.country }}</td>
        <td class="text-xs-center">{{ props.item.class }}</td>
      </tr>
    </template>
  </v-data-table>
</template>

<script>
import axios from "axios";

export default {
  name: "listCompetitions",
  methods: {
    rowClicked(item) {
      this.$router.push("/competitions/" + item.names);
    }
  },
  data() {
    return {
      competitions: [],
      headers: [
        { text: "Date", value: "date", align: "center" },
        { text: "Name", value: "names", align: "center", sortable: false},
        { text: "Country", value: "country", align: "center", sortable: false},
        { text: "Class", value: "class", align: "center" }
      ]
    };
  },
  mounted: function() {
    try {
      axios.get("http://192.168.1.5:2019/race/all")
        .then(res => {
          this.competitions = res.data;
          
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>