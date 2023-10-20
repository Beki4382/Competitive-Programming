class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        size = len(img1)
        max_overlap = 0
        coordinates_img1, coordinates_img2 = [], []
        
        for r in range(size):
            for c in range(size):
                if img1[r][c] == 1:
                    coordinates_img1.append((r, c))

                if img2[r][c] == 1:
                    coordinates_img2.append((r, c))

        overlap = {}
        for i1_r, i1_c in coordinates_img1:
            for i2_r, i2_c in coordinates_img2:
                shift = (i2_r - i1_r, i2_c - i1_c)
                overlap[shift] = overlap.get(shift, 0) + 1
                max_overlap = max(max_overlap, overlap[shift])

        return max_overlap
