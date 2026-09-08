class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        best_index = -1
        best_dist = float("inf")

        for i, (x, y, r) in enumerate(drones):
            dist = abs(x - tx) + abs(y - ty)
            if dist <= r:  # drone can reach target
                if dist < best_dist or (dist == best_dist and i < best_index):
                    best_dist = dist
                    best_index = i

        return best_index
        