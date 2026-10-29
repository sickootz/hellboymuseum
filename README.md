# Hellboy Museum

Independent fan-made archive for [@hellboy_museum](https://www.instagram.com/hellboy_museum/).

## Publish the site

Go to **Settings → Pages** in this repository. Set **Deploy from a branch → main → /(root)** and save. It should become available at https://sickootz.github.io/hellboymuseum/ once GitHub Pages builds.

## Add exhibits

1. Use **Add file → Upload files** on GitHub to upload your own photos into a folder called `images/` (create the folder if missing).
2. Open the site and click **+ Add exhibit**. Use an image path like `images/statue-01.jpg` and paste the caption and original Instagram post URL.
3. Click **Export collection.json** in the editor.
4. Upload the exported `collection.json` to the GitHub repository, replacing the existing file, and commit. Refresh the public page to see your new exhibits.

The editor stores changes in the current browser until exported. Instagram post URLs do not automatically import photos or descriptions, and they are not direct image URLs. Use only photos that you own or have permission to publish.


## Facebook archive imports

Keep one catalog entry for each identified object or set, using the existing categories. Compare repeat posts and set photographs before adding an exhibit. General museum views, teasers and unidentified objects remain outside the catalog until reviewed. Comic-inspired Skelton Crew artifact replicas belong in `Other`.

Each Facebook-imported entry must have its verified original post or photo-post URL in `source_url`, a matching button on its individual page, and a provenance entry in `facebook-sources.json`. Preserve the source photograph; use an optimized copy for the site. Do not invent missing specifications or treat edition-size rumors as established facts.

Before publication run `python scripts/check-facebook-sources.py`. The same check runs on GitHub pushes and pull requests. New pages must also be linked from the homepage and sitemap. Private export archives and editorial review files do not belong in the public repository.
