import unittest
import pygambit

from HypergameLib.src.HypergameLib import HNF


class MyTestCase(unittest.TestCase):
    def test_DesertStorm_hardcoded(self):
        """
        Hand-crafted test for Desert Storm Example.
        :return:
        """
        print("DESERT STORM EXAMPLE")
        g = pygambit.Game.new_table([6, 6])
        g.title = "Desert Storm Hypergame"
        g.players[0].label = "Attacker"
        g.players[1].label = "Defender"
        g.players[0].strategies[0].label = "Attack"
        g.players[0].strategies[1].label = "Attack Right"
        g.players[0].strategies[2].label = "Attack Left"
        g.players[0].strategies[3].label = "Env. Left"
        g.players[0].strategies[4].label = "Inv. Beach"
        g.players[0].strategies[5].label = "Env. Vert"

        g.players[1].strategies[0].label = "Defend"
        g.players[1].strategies[1].label = "Defend Left"
        g.players[1].strategies[2].label = "Defend Right"
        g.players[1].strategies[3].label = "W/ Res"
        g.players[1].strategies[4].label = "Screen"
        g.players[1].strategies[5].label = "Counter Attack"

        g[0, 0][g.players[0].label] = -1
        g[1, 0][g.players[0].label] = -1
        g[2, 0][g.players[0].label] = -1
        g[3, 0][g.players[0].label] = 3
        g[4, 0][g.players[0].label] = 1
        g[5, 0][g.players[0].label] = 2

        g[0, 0][g.players[1].label] = 1
        g[1, 0][g.players[1].label] = 1
        g[2, 0][g.players[1].label] = 1
        g[3, 0][g.players[1].label] = -3
        g[4, 0][g.players[1].label] = -1
        g[5, 0][g.players[1].label] = -2

        g[0, 1][g.players[0].label] = -1
        g[1, 1][g.players[0].label] = -3
        g[2, 1][g.players[0].label] = 0
        g[3, 1][g.players[0].label] = 5
        g[4, 1][g.players[0].label] = -3
        g[5, 1][g.players[0].label] = 0

        g[0, 1][g.players[1].label] = 1
        g[1, 1][g.players[1].label] = 3
        g[2, 1][g.players[1].label] = 0
        g[3, 1][g.players[1].label] = -5
        g[4, 1][g.players[1].label] = 3
        g[5, 1][g.players[1].label] = 0

        g[0, 2][g.players[0].label] = -1
        g[1, 2][g.players[0].label] = 0
        g[2, 2][g.players[0].label] = -3
        g[3, 2][g.players[0].label] = 1
        g[4, 2][g.players[0].label] = 2
        g[5, 2][g.players[0].label] = 0

        g[0, 2][g.players[1].label] = 1
        g[1, 2][g.players[1].label] = 0
        g[2, 2][g.players[1].label] = 3
        g[3, 2][g.players[1].label] = -1
        g[4, 2][g.players[1].label] = -2
        g[5, 2][g.players[1].label] = 0

        g[0, 3][g.players[0].label] = 1
        g[1, 3][g.players[0].label] = 1
        g[2, 3][g.players[0].label] = 1
        g[3, 3][g.players[0].label] = 2
        g[4, 3][g.players[0].label] = -1
        g[5, 3][g.players[0].label] = -3

        g[0, 3][g.players[1].label] = -1
        g[1, 3][g.players[1].label] = -1
        g[2, 3][g.players[1].label] = -1
        g[3, 3][g.players[1].label] = -2
        g[4, 3][g.players[1].label] = 1
        g[5, 3][g.players[1].label] = 3

        g[0, 4][g.players[0].label] = 1
        g[1, 4][g.players[0].label] = 1
        g[2, 4][g.players[0].label] = 1
        g[3, 4][g.players[0].label] = -1
        g[4, 4][g.players[0].label] = -1
        g[5, 4][g.players[0].label] = -2

        g[0, 4][g.players[1].label] = -1
        g[1, 4][g.players[1].label] = -1
        g[2, 4][g.players[1].label] = -1
        g[3, 4][g.players[1].label] = 1
        g[4, 4][g.players[1].label] = 1
        g[5, 4][g.players[1].label] = 2

        g[0, 5][g.players[0].label] = 4
        g[1, 5][g.players[0].label] = 1
        g[2, 5][g.players[0].label] = 1
        g[3, 5][g.players[0].label] = -2
        g[4, 5][g.players[0].label] = -2
        g[5, 5][g.players[0].label] = -1

        g[0, 5][g.players[1].label] = -4
        g[1, 5][g.players[1].label] = -1
        g[2, 5][g.players[1].label] = -1
        g[3, 5][g.players[1].label] = 2
        g[4, 5][g.players[1].label] = 2
        g[5, 5][g.players[1].label] = 1

        print("solver")
        s = pygambit.nash.enummixed_solve(g)

        # assert NEMS values for row player (calculated separately using Gambit GUI, asserted/tested here)
        self.assertAlmostEqual(float(s.equilibria[0][g.players[0]][g.players[0].strategies[0]]), 0.125, places=3,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[0]][g.players[0].strategies[1]]), 0.50, places=2,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[0]][g.players[0].strategies[2]]), 0.00, places=2,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[0]][g.players[0].strategies[3]]), 0.375, places=3,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[0]][g.players[0].strategies[4]]), 0.00, places=2,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[0]][g.players[0].strategies[5]]), 0.00, places=2,
                               msg="NEMS did not match")

        # assert NEMS values for column player (calculated separately using Gambit GUI, asserted/tested here)
        self.assertAlmostEqual(float(s.equilibria[0][g.players[1]][g.players[1].strategies[0]]), 0.00, places=2,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[1]][g.players[1].strategies[1]]), 0.125, places=3,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[1]][g.players[1].strategies[2]]), 0.25, places=2,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[1]][g.players[1].strategies[3]]), 0.00, places=2,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[1]][g.players[1].strategies[4]]), 0.625, places=3,
                               msg="NEMS did not match")
        self.assertAlmostEqual(float(s.equilibria[0][g.players[1]][g.players[1].strategies[5]]), 0.00, places=2,
                               msg="NEMS did not match")

    def test_simpleOPM(self):
        """
        DESC
            Display the HNF info created from file
        """
        simple_opm = HNF.HNFFactory("../../config/SimpleOPM").get_hnf_instance()
        simple_opm.display_hnf()
        for i, game in enumerate(simple_opm.gambitGames.values()):
            self.assertEqual(game.players[0].label, "Row Player", "Labels are incorrect")
            self.assertEqual(game.players[1].label, "Column Player", "Labels are incorrect")

            # get all the names of the strategies/actions
            actions_in_gambit = [i.label for i in game.strategies]

            # check that the actions in HNF and gambit match
            for rowAction in simple_opm.rowActionNames:
                self.assertTrue(rowAction in actions_in_gambit,
                                "Row action not found in gambit game")
            # for columnAction in simple_opm.columnActionNames:
            #    self.assertTrue(columnAction in actions_in_gambit,
            #                    "Column action not found in gambit game")

            # for col_ind, colName in enumerate(simple_opm.columnActionNames):
            #    for row_ind, rowName in enumerate(simple_opm.rowActionNames):
            #        self.assertEqual(float(game[row_ind, col_ind][0]), simple_opm.costs[colName][rowName])

            print("Calc the NEMS")
            s = pygambit.nash.logit_solve(game)
            print(s)
            # TODO: test not finished
            pass

    def test_DesertStorm(self):
        """
        DESC
            Display the HNF info created from file
        """
        DesertStormHNF = HNF.HNFFactory("../../config/DesertStormSettings").get_hnf_instance()
        DesertStormHNF.display_hnf()
        for i, game in enumerate(DesertStormHNF.gambitGames.values()):
            self.assertEqual(game.players[0].label, "Row Player", "Labels are incorrect")
            self.assertEqual(game.players[1].label, "Column Player", "Labels are incorrect")

            # get all the names of the strategies/actions
            actions_in_gambit = [g.label for g in game.strategies]

            # check that the actions in HNF and gambit match
            for rowAction in DesertStormHNF.rowActionNames:
                self.assertTrue(rowAction in actions_in_gambit,
                                "Row action not found in gambit game")

            # TODO: doesn't work because the 3x3 subgame doesn't have these actions because of the 'X' in config file
            for columnAction in DesertStormHNF.columnActionNames:
                self.assertTrue(columnAction in actions_in_gambit, "Column action not found in gambit game")

            # for col_ind, colName in enumerate(DesertStormHNF.columnActionNames):
            #     for row_ind, rowName in enumerate(DesertStormHNF.rowActionNames):
            #         # TODO: breaks when column indicator == 3 because it is testing the 3 x 3 subgame against the 6 x 6 actions
            #         self.assertEqual(float(game[row_ind, col_ind][game.players[0].label]), DesertStormHNF.costs_row[colName][rowName])

            print("Calc the NEMS")
            s = pygambit.nash.logit_solve(game)
            # equilibria now stored in a 3-d list?
            print(s)
            print(s.equilibria)
            print(type(s.equilibria))
            print(s.equilibria[0])
            print(type(s.equilibria[0]))
            # try iterating by player...
            print(s.equilibria[0][game.players[0]])
            print(s.equilibria[0][game.players[1]])
            print(type(s.equilibria[0][game.players[0]]))
            print(c for c in game.contingencies)

            # TODO: figure out why player1 has 6 actions and player2 only has 3
            # this first game in the loop has 9 strategies...doesn't seem right
            # is the 3x3 subgame really a 3x6 subgame?
            self.assertAlmostEqual(s.equilibria[0][0][0], 0.125, 3, msg="NEMS does not match expectation")
            self.assertAlmostEqual(s.equilibria[0][0][1], 0.5, 1, msg="NEMS does not match expectation")
            self.assertAlmostEqual(s.equilibria[0][0][2], 0.0, 1, msg="NEMS does not match expectation")
            self.assertAlmostEqual(s.equilibria[0][0][3], 0.375, 3, msg="NEMS does not match expectation")
            pass


if __name__ == '__main__':
    unittest.main()
