/* Dashboard template, theme switch and chart styling.

   Presentation only: this file knows nothing about any product's data. It
   provides
   - the three-state theme switch (auto / light / dark) on [data-theme-choice]
     buttons, remembered per browser,
   - Dash.layout(extra): the base Plotly layout read from the CSS tokens
     (transparent surfaces, no grid lines, muted axes),
   - Dash.plot(el, data, layout): Plotly.newPlot with that base layout,
   - Dash.retheme(): re-colours every chart on the page after a theme change,
     including charts rendered server-side by plotly.py.

   A trace whose colour has to follow the text colour (a black "actual" line
   that would vanish in dark mode) carries meta: 'ink'; Dash.retheme repaints
   it. Other trace colours come from the gemstone tokens and read in both
   themes. The storage key comes from <html data-theme-key>, so two dashboards
   opened side by side do not share one setting unless they want to. */
(function () {
  'use strict';
  var Dash = window.Dash = window.Dash || {};
  var root = document.documentElement;
  var KEY = root.getAttribute('data-theme-key') || 'dash-theme';

  Dash.css = function (name) { return getComputedStyle(root).getPropertyValue(name).trim(); };
  Dash.PLOT_CONFIG = {displaylogo: false, responsive: true, modeBarButtonsToRemove: ['lasso2d', 'select2d', 'autoScale2d']};

  function isObj(v) { return v && typeof v === 'object' && !Array.isArray(v); }
  function deepMerge(a, b) {
    Object.keys(b || {}).forEach(function (k) {
      if (isObj(b[k]) && isObj(a[k])) { deepMerge(a[k], b[k]); } else { a[k] = b[k]; }
    });
    return a;
  }
  Dash.merge = deepMerge;

  function axisTheme() {
    var line = Dash.css('--border');
    return {showgrid: false, zeroline: false, linecolor: line, tickcolor: line, color: Dash.css('--muted')};
  }
  Dash.layout = function (extra) {
    var text = Dash.css('--text'), line = Dash.css('--border');
    var base = {
      paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
      font: {family: getComputedStyle(document.body).fontFamily, size: 12, color: text},
      title: {x: 0, xanchor: 'left', font: {size: 14, color: text}},
      margin: {t: 24, r: 16, b: 48, l: 64},
      xaxis: axisTheme(), yaxis: axisTheme(),
      legend: {orientation: 'h', y: -0.18, font: {size: 11, color: text}},
      hoverlabel: {bgcolor: Dash.css('--card-bg'), bordercolor: line, font: {color: text, size: 12}}
    };
    extra = extra || {};
    Object.keys(extra).forEach(function (k) {
      if (/^[xy]axis\d+$/.test(k) && !base[k]) { base[k] = axisTheme(); }
    });
    return deepMerge(base, extra);
  };
  Dash.plot = function (el, data, layout, config) {
    if (typeof el === 'string') { el = document.getElementById(el); }
    if (!el || !window.Plotly) { return null; }
    return Plotly.newPlot(el, data, Dash.layout(layout), deepMerge(deepMerge({}, Dash.PLOT_CONFIG), config || {}));
  };

  /* Only colours are touched, so a chart keeps its own titles, ranges and
     annotations; the same call serves plotly.py figures and Dash.plot charts. */
  Dash.retheme = function () {
    if (!window.Plotly) { return; }
    var text = Dash.css('--text'), muted = Dash.css('--muted'), line = Dash.css('--border');
    document.querySelectorAll('.js-plotly-plot').forEach(function (gd) {
      if (!gd.layout) { return; }
      var upd = {
        paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
        'font.color': text, 'title.font.color': text, 'legend.font.color': text,
        'hoverlabel.bgcolor': Dash.css('--card-bg'), 'hoverlabel.bordercolor': line, 'hoverlabel.font.color': text
      };
      Object.keys(gd.layout).forEach(function (k) {
        if (/^[xy]axis\d*$/.test(k)) {
          upd[k + '.color'] = muted; upd[k + '.linecolor'] = line; upd[k + '.tickcolor'] = line;
          upd[k + '.gridcolor'] = line; upd[k + '.zerolinecolor'] = line;
        }
      });
      Plotly.relayout(gd, upd);
      var ink = [];
      (gd.data || []).forEach(function (t, i) { if (t.meta === 'ink') { ink.push(i); } });
      if (ink.length) { Plotly.restyle(gd, {'line.color': text, 'marker.color': text}, ink); }
    });
  };

  function storedTheme() { try { return localStorage.getItem(KEY) || 'auto'; } catch (e) { return 'auto'; } }
  function applyTheme(choice) {
    var dark = choice === 'dark' || (choice === 'auto' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
    var before = root.getAttribute('data-theme');
    root.setAttribute('data-theme', dark ? 'dark' : 'light');
    document.querySelectorAll('[data-theme-choice]').forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-theme-choice') === choice);
    });
    if (before !== root.getAttribute('data-theme')) {
      Dash.retheme();
      document.dispatchEvent(new CustomEvent('dash:theme', {detail: {theme: root.getAttribute('data-theme')}}));
    }
  }
  Dash.initTheme = function () {
    document.querySelectorAll('[data-theme-choice]').forEach(function (b) {
      b.addEventListener('click', function () {
        var c = b.getAttribute('data-theme-choice');
        try { localStorage.setItem(KEY, c); } catch (e) { /* private window: applies to this view only */ }
        applyTheme(c);
      });
    });
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
        if (storedTheme() === 'auto') { applyTheme('auto'); }
      });
    }
    applyTheme(storedTheme());
    // plotly.py figures are drawn before this runs, with light colours baked
    // in; one pass brings them onto the tokens of the active theme.
    Dash.retheme();
  };
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', Dash.initTheme); }
  else { Dash.initTheme(); }
})();
