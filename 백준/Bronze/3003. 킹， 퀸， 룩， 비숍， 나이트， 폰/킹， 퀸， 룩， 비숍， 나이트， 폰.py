king, queen, rook, bishop, knight, pawn = map(int, input().split())
actual_king_num = 1
actual_queen_num = 1
actual_rook_num = 2
actual_bishop_num = 2
actual_knight_num = 2
actual_pawn_num = 8
print(actual_king_num - king, actual_queen_num - queen, actual_rook_num - rook, actual_bishop_num - bishop, actual_knight_num - knight, actual_pawn_num - pawn)