from manim import *
import numpy as np

# Colores inspirados en Datos de Ciencia
SOLAR_ORANGE = "#E85D24"
PLASMA_AMBER = "#F5A623"
CORONA_YELLOW = "#FCDE5A"
DARK_BG = "#0D1117"
GRID_COLOR = "#FCDE5A"
BBOX_COLOR = "#E85D24"
CONF_COLOR = "#F5A623"
TEXT_COLOR = "#FFFFFF"


class YOLOGridAnimation(Scene):
    def construct(self):
        self.camera.background_color = DARK_BG

        # ── 1. Título ──────────────────────────────────────────────────────────
        title = Text("¿Cómo ve YOLO una imagen?", font_size=42, color=TEXT_COLOR)
        subtitle = Text("You Only Look Once", font_size=22, color=PLASMA_AMBER)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── 2. Imagen de entrada (rectángulo simulando foto) ───────────────────
        image_rect = Rectangle(width=5.5, height=4.0, color=WHITE, fill_opacity=0.08)
        image_rect.shift(LEFT * 1.5)

        img_label = Text("Imagen de entrada", font_size=20, color=TEXT_COLOR)
        img_label.next_to(image_rect, UP, buff=0.3)

        # Objetos simulados dentro de la imagen (siluetas de carros desde arriba)
        car1 = Rectangle(width=0.5, height=0.9, color=CONF_COLOR, fill_opacity=0.35)
        car1.move_to(image_rect.get_center() + LEFT * 1.2 + UP * 0.8)

        car2 = Rectangle(width=0.5, height=0.9, color=CONF_COLOR, fill_opacity=0.35)
        car2.move_to(image_rect.get_center() + RIGHT * 0.4 + DOWN * 0.5)

        car3 = Rectangle(width=0.5, height=0.9, color=CONF_COLOR, fill_opacity=0.35)
        car3.move_to(image_rect.get_center() + LEFT * 0.3 + UP * 0.2)

        self.play(FadeIn(image_rect), Write(img_label))
        self.play(FadeIn(car1), FadeIn(car2), FadeIn(car3))
        self.wait(0.8)

        # ── 3. Grid SxS aparece sobre la imagen ───────────────────────────────
        S = 7  # grid 7x7
        grid_lines = VGroup()
        left = image_rect.get_left()[0]
        right = image_rect.get_right()[0]
        bottom = image_rect.get_bottom()[1]
        top = image_rect.get_top()[1]
        w = right - left
        h = top - bottom

        for i in range(1, S):
            x = left + i * w / S
            vline = Line([x, bottom, 0], [x, top, 0], color=GRID_COLOR, stroke_width=1.2)
            grid_lines.add(vline)
        for j in range(1, S):
            y = bottom + j * h / S
            hline = Line([left, y, 0], [right, y, 0], color=GRID_COLOR, stroke_width=1.2)
            grid_lines.add(hline)

        grid_label = Text(f"Grid {S}×{S}", font_size=20, color=GRID_COLOR)
        grid_label.next_to(image_rect, DOWN, buff=0.3)

        self.play(
            Create(grid_lines, run_time=1.5, lag_ratio=0.05),
            Write(grid_label),
        )
        self.wait(0.8)

        # ── 4. Resaltar una celda responsable de detectar car1 ────────────────
        # Celda aproximada donde está car1
        col = 1  # 0-indexed
        row = 5  # 0-indexed (desde arriba)
        cell_x = left + (col + 0.5) * w / S
        cell_y = top - (row + 0.5) * h / S
        cell_w = w / S
        cell_h = h / S

        active_cell = Rectangle(
            width=cell_w, height=cell_h,
            color=SOLAR_ORANGE, fill_opacity=0.45, stroke_width=2.5
        )
        active_cell.move_to([cell_x, cell_y, 0])

        cell_note = Text("Celda responsable\nde este objeto", font_size=16, color=SOLAR_ORANGE)
        cell_note.next_to(image_rect, RIGHT, buff=0.4).shift(UP * 1.0)
        arrow_cell = Arrow(
            cell_note.get_left(), active_cell.get_center(),
            color=SOLAR_ORANGE, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )

        self.play(FadeIn(active_cell, scale=1.3))
        self.play(Write(cell_note), GrowArrow(arrow_cell))
        self.wait(1.2)

        # ── 5. Vector de predicción por celda ─────────────────────────────────
        self.play(
            FadeOut(cell_note), FadeOut(arrow_cell),
            FadeOut(active_cell),
        )

        pred_title = Text("Cada celda predice un vector:", font_size=22, color=TEXT_COLOR)
        pred_title.to_edge(RIGHT, buff=0.5).shift(UP * 2.8)

        # Vector components
        components = [
            (r"x,\, y", "Centro del bbox", CORONA_YELLOW),
            (r"w,\, h", "Ancho y alto", CORONA_YELLOW),
            (r"p_c", "Confianza de objeto", PLASMA_AMBER),
            (r"c_1, \ldots, c_n", "Clase del objeto", SOLAR_ORANGE),
        ]

        vec_group = VGroup()
        for i, (math_str, desc_str, col) in enumerate(components):
            math_mob = MathTex(math_str, font_size=28, color=col)
            desc_mob = Text(desc_str, font_size=16, color=TEXT_COLOR)
            desc_mob.next_to(math_mob, RIGHT, buff=0.3)
            row_group = VGroup(math_mob, desc_mob)
            row_group.shift(DOWN * i * 0.65)
            vec_group.add(row_group)

        vec_group.next_to(pred_title, DOWN, buff=0.4).align_to(pred_title, LEFT)

        self.play(Write(pred_title))
        for row_g in vec_group:
            self.play(FadeIn(row_g, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(1.0)

        # ── 6. Bounding boxes finales ──────────────────────────────────────────
        self.play(FadeOut(vec_group), FadeOut(pred_title))

        bbox1 = SurroundingRectangle(car1, color=BBOX_COLOR, buff=0.08, stroke_width=2.5)
        bbox2 = SurroundingRectangle(car2, color=BBOX_COLOR, buff=0.08, stroke_width=2.5)
        bbox3 = SurroundingRectangle(car3, color=BBOX_COLOR, buff=0.08, stroke_width=2.5)

        conf1 = Text("0.91", font_size=14, color=BBOX_COLOR)
        conf1.next_to(bbox1, UP, buff=0.05)
        conf2 = Text("0.87", font_size=14, color=BBOX_COLOR)
        conf2.next_to(bbox2, UP, buff=0.05)
        conf3 = Text("0.83", font_size=14, color=BBOX_COLOR)
        conf3.next_to(bbox3, UP, buff=0.05)

        result_label = Text("Detecciones finales", font_size=22, color=BBOX_COLOR)
        result_label.to_edge(RIGHT, buff=0.5).shift(UP * 1.5)

        self.play(
            Create(bbox1), Create(bbox2), Create(bbox3),
            FadeIn(conf1), FadeIn(conf2), FadeIn(conf3),
            run_time=1.2,
        )
        self.play(Write(result_label))
        self.wait(1.5)

        # ── 7. Frase final ────────────────────────────────────────────────────
        self.play(
            FadeOut(grid_lines), FadeOut(grid_label),
            FadeOut(bbox1), FadeOut(bbox2), FadeOut(bbox3),
            FadeOut(conf1), FadeOut(conf2), FadeOut(conf3),
            FadeOut(car1), FadeOut(car2), FadeOut(car3),
            FadeOut(image_rect), FadeOut(img_label),
            FadeOut(result_label),
        )

        final = Text(
            "Una sola pasada por la red.\nToda la imagen al mismo tiempo.",
            font_size=34, color=TEXT_COLOR,
            line_spacing=1.4,
        )
        final.set_color_by_gradient(PLASMA_AMBER, SOLAR_ORANGE)
        self.play(Write(final, run_time=2.0))
        self.wait(2)
        self.play(FadeOut(final))