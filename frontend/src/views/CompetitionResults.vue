<template>
  <v-container grid-list-xs>
    <v-layout row wrap>
      <ListStages/>
    </v-layout>
    <v-layout row wrap>
      <v-flex x12 md12>
        <h1 align="center">Final Classifications of {{this.$route.params.id}}</h1>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex x12 md12>
        <General/>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex x12 md12>
        <Points/>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex x12 md12>
        <Mountain/>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex x12 md12>
        <Youth/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import General from "../components/competitions/General";
import Points from "../components/competitions/Points";
import Mountain from "../components/competitions/Mountain";
import Youth from "../components/competitions/Youth";
import ListStages from "../components/competitions/ListStages";

export default {
  name: "competitionResults",
  components: {
    General,
    Points,
    Mountain,
    Youth,
    ListStages
  }
};
</script>
