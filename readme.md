# Kra2Png Documentation

## Kra2Png – Batch Export .kra Files to .png

**Kra2Png** is a Krita plugin that allows you to quickly export all `.kra` files in a selected folder as flattened `.png` images.

This is useful for:

- Archiving or sharing your artwork outside Krita
- Batch-exporting work for external tools or pipelines
- Reducing time spent manually opening and exporting each file

## Usage

1. Go to **Tools > Scripts > Batch Export .kra to PNG** (or wherever you installed it).
2. First popup: Select the folder containing your `.kra` files.
3. The plugin will create a subfolder called `Exported_PNGs` inside that folder (automatically).
4. All `.kra` files will be opened in the background and exported as `.png` into the new subfolder.

During the export, small notification "toasts" will appear to indicate progress. Once complete, you’ll see a confirmation message.

## Notes

- PNG export includes transparency and uses maximum compression (level 9).
- Files are processed in batch mode — documents are not shown or modified.
- Only files ending in `.kra` (not subfolders) will be processed.
