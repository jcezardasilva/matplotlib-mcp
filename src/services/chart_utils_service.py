from __future__ import annotations

import io

import matplotlib
import matplotlib.pyplot as plt
from mcp.server.fastmcp import Image


matplotlib.use("Agg")


def create_figure(width: int, height: int, dpi: int):
	width_in = width / dpi
	height_in = height / dpi
	return plt.subplots(figsize=(width_in, height_in), dpi=dpi)


def apply_common_axes_settings(
	ax,
	*,
	title: str | None = None,
	x_label: str | None = None,
	y_label: str | None = None,
	legend: bool = False,
) -> None:
	if title:
		ax.set_title(title)
	if x_label:
		ax.set_xlabel(x_label)
	if y_label:
		ax.set_ylabel(y_label)
	if legend:
		ax.legend()


def finalize_figure(fig, image_format: str) -> Image:
	fig.tight_layout()
	buffer = io.BytesIO()
	fig.savefig(buffer, format=image_format)
	plt.close(fig)
	return Image(data=buffer.getvalue(), format=image_format)
