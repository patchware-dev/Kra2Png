# Kra2Png Documentation

## Kra2Png – Batch Export .kra Files to .png

**Kra2Png** is a Krita plugin that allows you to quickly export all `.kra` files in a selected folder as flattened `.png` images. I use this for quickly exporting every page of my in-progress comic.

You may find this useful for:
- Archiving or sharing your artwork outside Krita
- Batch-exporting work for external tools or pipelines
- Reducing time spent manually opening and exporting each file

## How To Install a Krita Plugin
1. Locate Krita’s pykrita folder:
- Linux: ~/.local/share/krita/pykrita/
- Windows: C:\Users\<YourName>\AppData\Roaming\krita\pykrita\
- macOS: ~/Library/Application Support/Krita/pykrita/
2. Copy the *Kra2Png folder* and the *Kra2Png.desktop* file into *pykrita/* (You don't need the gitignore or readme files!)
3. Restart Krita
4. Activate the plugin
- Go to Settings > Configure Krita > Python Plugin Manager
- Find Kra2Png in the list and check the box to enable it
- Click OK and restart Krita again if needed

## Usage
1. Go to **Tools > Scripts > Export all KRA files in folder as PNG** (or wherever you installed it).
2. First popup: Select the folder containing your `.kra` files.
3. The plugin will create a subfolder called `Exported_PNGs` inside that folder (automatically).
4. All `.kra` files will be opened in the background and exported as `.png` into the new subfolder.

During the export, small notification "toasts" will appear to indicate progress. Once complete, you’ll see a confirmation message. The exported PNGs are in a newly created subfolder in the folder that your KRAs are in.

## Notes

- PNG export includes transparency and uses maximum compression (level 9).
- Files are processed in batch mode — documents are not shown or modified.
- Only files ending in `.kra` (not subfolders) will be processed.
