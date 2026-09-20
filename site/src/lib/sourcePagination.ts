export const SOURCES_PER_PAGE = 150;

export function sourcePageCount(totalSources: number): number {
  return Math.max(1, Math.ceil(totalSources / SOURCES_PER_PAGE));
}

export function sourcePageHref(base: string, pageNumber: number): string {
  return pageNumber === 1
    ? `${base}sources/`
    : `${base}sources/page/${pageNumber}/`;
}
