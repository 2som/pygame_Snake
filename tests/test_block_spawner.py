from src.objects.BlockSpawner import BlockSpawner
from Config import Config

class TestBlockSpawner:
    def test_spawned_coords_are_random_enough(self):
        spawner = BlockSpawner(Config())
        
        spawner.last_spawned_positions = [
            {"x": 100, "y": 200},
        ]

        assert spawner._check_if_random_coords_are_random_enough(150, 200) == False
        assert spawner._check_if_random_coords_are_random_enough(100, 401) == True

    def test_spawner_remembers_only_last_3_positions(self):
        spawner = BlockSpawner(Config())
        spawner.last_spawned_positions = [
            {"x": 100, "y": 200},
            {"x": 250, "y": 300},
            {"x": 26, "y": 700 }
        ]

        spawner._generate_random_position()

        assert len(spawner.last_spawned_positions) == 3