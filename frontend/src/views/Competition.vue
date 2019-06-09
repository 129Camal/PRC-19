<template>
  <v-container grid-list-xs>
    <ListCompetitions/>
  </v-container>
</template>

<script>
import ListCompetitions from "../components/competitions/ListCompetitions";

export default {
  name: "competitions",
  components: {
    ListCompetitions
  }
};
</script>
