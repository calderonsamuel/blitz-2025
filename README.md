You can use `uv` to bootstrap this project. Intitalize a virtual environment with `uv venv`, activate it, then run `uv sync`.

- obtencion.py has the manual process for extracting the data
- trabajo_individual.ipynb is the only thing you need to run for the analysis. The data folder already has the processed data you need for the project.

## Processed dataset dictionary

The preprocessed dataset (`data/preprocessed.parquet`) has 3,149,830 rows and 14 columns. It is a panel dataset where each row represents one player in one month.

The following transformations were applied to the raw data: `title` and `w_title` were merged into a single `title` column; `o_title`, `foa_title`, and `Unnamed: 0` were dropped; `filename` was replaced by a `month` integer (1–12); `flag` was decoded into a boolean `active` column; `birthday` was renamed to `birth_year`; and three derived columns (`age`, `age_group`, `rating_category`) were added.

| Column | Type | Description |
|---|---|---|
| `fideid` | int | Player identification number in the FIDE database |
| `name` | str | Player name |
| `country` | str | National federation the player belongs to |
| `sex` | str | Player sex (M = male, F = female) |
| `title` | str | OTB chess title (GM, IM, FM, CM, WGM, WIM, WFM, WCM); consolidated from the original `title` and `w_title` columns; null if the player holds no title |
| `rating` | int | Player's Blitz Elo rating |
| `games` | int | Number of Blitz games played in the corresponding period |
| `k` | int | K-factor of the Elo system: 40 = new player (< 30 games or under 18), 20 = standard, 10 = elite (ever exceeded 2400) |
| `birth_year` | float | Player's year of birth; null for ~1.1% of records |
| `month` | int | Month of the record (1–12), extracted from the source filename |
| `active` | bool | Whether the player was active in that period (True/False), decoded from the original `flag` column |
| `age` | Int64 | Player's age in 2025 (2025 − birth_year); null when `birth_year` is missing |
| `age_group` | category | Age group: ≤14, 15-18, 19-25, 26-35, 36-50, 51-65, 65+ |
| `rating_category` | category | Rating level: Principiante (< 1500), Intermedio (1500–1800), Avanzado (1800–2100), Experto (2100–2400), Élite (≥ 2400) |