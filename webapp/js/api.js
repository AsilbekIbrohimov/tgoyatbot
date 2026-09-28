// API so'rovlari (kesh bilan)
const cache = {};

export async function jget(url) {
  if (cache[url]) return cache[url];
  const r = await fetch(url);
  if (!r.ok) throw new Error('network');
  const j = await r.json();
  cache[url] = (j.data !== undefined) ? j.data : j;
  return cache[url];
}
