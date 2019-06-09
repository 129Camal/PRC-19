<template>
  <v-container grid-list-xs>
    <h1>Final Classifications of {{this.$route.params.id}}</h1>
    <General/>
    <Points/>
    <Mountain/>
    <Youth/>
  </v-container>
</template>

<script>
import General from "../components/competitions/General";
import Points from "../components/competitions/Points";
import Mountain from "../components/competitions/Mountain";
import Youth from "../components/competitions/Youth";

export default {
  name: "competitionResults",
  components: {
    General,
    Points,
    Mountain,
    Youth
  }
};
</script>
