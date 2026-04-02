# Stage 04: Progress Tracking & Collection

Monitor production status and collect outputs from completed workflows.

## Objective

Track the status of dispatched production agents, update campaign status as deliverables complete, and collect all manifest files once both tracks finish.

## Progress Tracking

After dispatch, monitor completion by checking for output artifacts:

### Design Track Completion Signals
- `design-manifest.json` exists in the campaign output folder
- Individual asset files (PNG/JPG/PDF/SVG) present at expected paths
- Designer's status updates in the campaign folder

### Video Track Completion Signals
- `video-manifest.json` exists in the campaign output folder
- Video files (MP4) present at expected paths
- Video Producer's status updates in the campaign folder

### Status Updates

As each deliverable completes, update `status.md`:
- Mark individual deliverables as `complete` or `failed`
- Increment `deliverables_complete` in frontmatter
- When all design deliverables finish: `design_track: 'complete'`
- When all video deliverables finish: `video_track: 'complete'`

## Collection

Once both tracks report complete (or one track was empty):

1. **Gather manifests:**
   - Read `design-manifest.json` — list of all visual assets with paths, dimensions, platforms
   - Read `video-manifest.json` — list of all video assets with paths, codec, resolution, duration
   
2. **Verify asset existence:** For each asset listed in the manifests, confirm the file exists at the specified path. Flag any missing files.

3. **Build consolidated asset inventory:**
   
   Update `status.md` with a `## Produced Assets` section:
   ```markdown
   ### Design Assets
   - [asset-name] — [platform] — [dimensions] — [path] — [status: verified/missing]
   
   ### Video Assets  
   - [asset-name] — [platform] — [resolution/duration] — [path] — [status: verified/missing]
   ```

4. **Handle failures:** If any deliverables failed:
   - Record failure reason in status
   - If not headless, ask user whether to retry, skip, or abort
   - If headless, log failures and continue with successful assets

## Output

Update `status.md`:
- Update frontmatter: `current_stage: '04-progress-collection'`, `status: 'quality-gate'`
- Append daily log: `[Campaign] Production complete for {campaign-name}: {n} design assets, {m} video assets, {f} failures`

Then load `./references/05-quality-completion.md`.
