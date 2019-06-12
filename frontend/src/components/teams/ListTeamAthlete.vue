<template>
  <v-flex xs12 md5>
    <h1 align="center">Athletes</h1>
    <v-data-table :headers="headers" :items="members" class="elevation-1">
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
      </template>

      <template slot="items" slot-scope="props">
        <tr @click="rowClicked(props.item)">
          <td class="text-xs-center">{{ props.item.name}}</td>
          <td class="text-xs-center">
            <country-flag :country="props.item.country" size="normal"/>
          </td>
        </tr>
      </template>
    </v-data-table>
  </v-flex>
</template>

<script>
import axios from "axios";
import CountryFlag from "vue-country-flag";

export default {
  name: "listTeamMembers",
  components: {
    CountryFlag
  },
  methods: {
    rowClicked(item) {
      this.$router.push("/members/" + item.ath.split("_")[1]);
    }
  },
  data() {
    return {
      members: [],
      headers: [
        { text: "Name", value: "name", align: "center" },
        { text: "Country", value: "country", align: "center", sortable: false }
      ]
    };
  },
  mounted: function() {
    try {
      axios
        .get(
          "http://192.168.1.83:2019/team/" + this.$route.params.id + "/athlete"
        )
        .then(res => {
          this.members = res.data;
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>