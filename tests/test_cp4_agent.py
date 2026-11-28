"""Kiểm tra các lớp phân tích và tra cứu trước lượt đánh giá CP4."""
import os
import sys
import unittest
from pathlib import Path

os.environ["MODEL_PROVIDER"] = "fake"
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codebase"))
import agent
from tools import tra_dieu_khoan


class AgentCP4Tests(unittest.TestCase):
    def test_formatted_conclusion(self):
        for line in ("KẾT LUẬN: Chưa đủ điều kiện", "**KẾT LUẬN:** Chưa đủ điều kiện",
                     "**KẾT LUẬN: Chưa đủ điều kiện**"):
            label, codes, errors = agent.kiem_can_cu(line + "\nTheo [SP-05].")
            self.assertEqual((label, codes, errors), (agent.CHUA_DU, ["SP-05"], []))

    def test_unknown_citation_still_rejected(self):
        self.assertTrue(agent.kiem_can_cu("**KẾT LUẬN:** Đủ điều kiện [SP-99]")[2])

    def test_partial_negation_does_not_erase_existing_evidence(self):
        for text in ("Đã quay clip lúc nhận nhưng chưa quay khi thử máy",
                     "Không quay video nhưng đã chụp ảnh khi nhận"):
            self.assertNotEqual(agent.tach_thong_tin(text)["bang_chung"], "không")
        self.assertEqual(agent.tach_thong_tin("Chưa quay video khi nhận")["bang_chung"], "không")

    def test_retrieval_for_distinct_user_phrasings(self):
        examples = (
            ("Màu sản phẩm lệch so với hình, gửi trả mất phí không?", {"SP-07", "SP-28"}),
            ("Người bán bảo liên hệ qua Zalo", {"SP-35"}),
            ("Shop im lặng, tự sắp xếp vận chuyển", {"SP-23", "SP-30"}),
        )
        for question, expected in examples:
            topics = agent.tach_thong_tin(question)["chu_de"]
            found = {clause["code"] for clause in tra_dieu_khoan(topics)}
            self.assertTrue(expected <= found, (question, expected - found))


if __name__ == "__main__":
    unittest.main()
