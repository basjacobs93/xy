from shapely import geometry, ops
import xy

PATHS = [
    "M176.718,548.268 L173.485,546.418 L170.279,544.341 L167.099,542.037 L163.944,539.504 L160.813,536.743 L157.706,533.751 L154.62,530.529 L151.556,527.075 L147.157,522.125 L141.483,516.014 L128.357,502.397 L116.286,490.397 L111.929,486.309 L109.376,484.191 L108.331,483.794 L106.522,483.426 L100.955,482.785 L93.361,482.287 L84.429,481.95 L74.848,481.792 L65.306,481.831 L56.492,482.087 L49.094,482.577 L42.56,483.146 L38.755,483.25 L37.554,483.11 L36.648,482.834 L35.909,482.414 L35.206,481.844 L33.929,480.534 L32.861,479.083 L31.996,477.519 L31.333,475.872 L30.868,474.17 L30.597,472.441 L30.517,470.714 L30.625,469.016 L30.916,467.378 L31.389,465.826 L32.038,464.39 L32.862,463.098 L33.856,461.978 L35.017,461.059 L36.342,460.369 L37.827,459.937 L39.445,459.768 L41.247,459.796 L43.014,460.006 L44.524,460.383 L46.265,460.813 L48.659,461.165 L51.39,461.402 L54.143,461.49 L57.531,461.422 L59.557,461.142 L60.183,460.887 L60.618,460.536 L60.91,460.075 L61.11,459.49 L61.381,458.713 L61.733,458.077 L62.12,457.648 L62.496,457.49 L63.007,457.154 L63.761,456.241 L64.656,454.89 L65.591,453.24 L66.65,450.869 L67.345,448.374 L67.73,445.479 L67.861,441.907 L67.784,437.892 L67.616,436.38 L67.319,435.045 L66.857,433.773 L66.198,432.448 L64.155,429.18 L62.345,426.617 L60.186,423.812 L57.949,421.104 L55.905,418.833 L52.723,415.308 L51.755,414.076 L51.4,413.434 L51.246,413.113 L50.807,412.622 L49.202,411.221 L44.005,407.378 L37.908,403.365 L35.178,401.751 L33.009,400.641 L30.345,399.383 L29.525,398.831 L28.976,398.22 L28.643,397.466 L28.472,396.485 L28.4,393.509 L28.517,390.603 L28.726,389.501 L29.091,388.516 L29.655,387.56 L30.459,386.545 L32.956,383.987 L35.889,381.43 L37.273,380.458 L38.608,379.692 L39.896,379.132 L41.142,378.779 L42.351,378.632 L43.525,378.694 L44.669,378.963 L45.787,379.442 L46.883,380.13 L47.961,381.028 L49.024,382.136 L50.077,383.456 L52.167,386.731 L53.537,388.875 L55.42,391.442 L59.963,396.971 L62.241,399.495 L64.269,401.569 L65.856,402.973 L66.424,403.356 L66.811,403.49 L67.364,403.786 L68.373,404.591 L71.19,407.24 L76.436,412.235 L78.93,414.38 L81.315,416.271 L83.572,417.894 L85.684,419.238 L87.633,420.286 L89.4,421.027 L91.88,421.759 L94.685,422.372 L97.627,422.848 L100.518,423.172 L103.17,423.328 L105.396,423.3 L107.008,423.07 L107.525,422.875 L107.818,422.623 L108.37,422.183 L109.357,421.823 L110.637,421.579 L112.073,421.49 L113.75,421.323 L115.69,420.868 L117.652,420.194 L119.396,419.372 L120.754,418.449 L122.137,417.226 L123.481,415.791 L124.723,414.23 L125.799,412.628 L126.646,411.074 L127.201,409.652 L127.4,408.45 L127.627,407.153 L128.246,405.403 L129.164,403.371 L130.286,401.225 L131.519,399.132 L132.769,397.263 L133.943,395.785 L134.946,394.868 L136.185,394.237 L137.584,393.852 L139.118,393.709 L140.762,393.805 L142.491,394.136 L144.281,394.701 L146.106,395.495 L147.941,396.515 L149.023,397.261 L149.913,398.044 L150.614,398.874 L151.13,399.758 L151.464,400.703 L151.62,401.719 L151.603,402.811 L151.414,403.99 L150.844,409.626 L149.752,424.21 L149.565,428.084 L149.724,430.837 L149.961,431.977 L150.318,433.059 L151.437,435.342 L152.63,437.142 L154.078,438.759 L155.766,440.187 L157.683,441.417 L159.814,442.443 L162.146,443.257 L164.666,443.852 L167.36,444.22 L170.626,444.434 L173.573,444.44 L176.278,444.219 L178.817,443.751 L181.268,443.019 L183.708,442.005 L186.212,440.689 L188.858,439.053 L192.625,436.662 L193.967,435.94 L195.089,435.489 L196.096,435.276 L197.095,435.269 L199.487,435.74 L201.652,436.458 L202.524,436.929 L203.311,437.523 L204.056,438.279 L204.799,439.231 L206.448,441.876 L207.588,443.992 L208.522,445.975 L209.156,447.601 L209.391,448.648 L209.031,449.665 L208.045,451.21 L206.584,453.072 L204.798,455.041 L202.41,457.572 L200.507,459.784 L199.039,461.786 L197.954,463.682 L197.199,465.58 L196.724,467.587 L196.476,469.809 L196.404,472.354 L196.467,474.542 L196.664,476.574 L196.998,478.455 L197.473,480.188 L198.093,481.778 L198.864,483.229 L199.788,484.544 L200.871,485.728 L202.116,486.785 L203.529,487.719 L205.112,488.535 L206.871,489.235 L208.809,489.825 L210.931,490.308 L213.242,490.689 L215.744,490.971 L219.154,491.347 L221.84,491.839 L223.885,492.523 L224.693,492.959 L225.372,493.471 L225.932,494.068 L226.384,494.759 L226.737,495.553 L227.004,496.46 L227.315,498.649 L227.4,501.401 L227.313,504.665 L227.164,505.831 L226.91,506.783 L226.526,507.594 L225.984,508.336 L224.323,509.901 L222.42,511.294 L221.462,511.75 L220.369,512.074 L219.045,512.288 L217.392,512.415 L212.709,512.49 L210.009,512.541 L207.553,512.705 L205.327,512.996 L203.318,513.429 L201.51,514.019 L199.89,514.78 L198.443,515.727 L197.156,516.875 L196.013,518.238 L195.002,519.831 L194.107,521.668 L193.314,523.766 L192.61,526.137 L191.979,528.797 L190.884,535.041 L190.161,539.392 L189.383,543.144 L188.645,545.898 L188.319,546.775 L188.039,547.251 L186.944,548.175 L185.699,548.875 L184.334,549.352 L182.877,549.6 L181.358,549.619 L179.806,549.405 L178.249,548.955 L176.718,548.268 L176.718,548.268",
    "M481.172,441.422 L480.25,440.66 L479.015,439.327 L477.63,437.612 L476.254,435.703 L472.949,431.157 L469.482,426.845 L466.185,422.765 L463.287,418.774 L461.993,417.117 L460.402,415.508 L458.716,414.13 L457.136,413.169 L455.266,412.499 L452.947,412.007 L450.327,411.693 L447.554,411.561 L444.776,411.611 L442.142,411.847 L439.801,412.271 L437.9,412.885 L436.168,413.521 L435.47,413.619 L434.804,413.552 L434.112,413.306 L433.333,412.868 L431.279,411.358 L429.714,410 L428.38,408.573 L427.296,407.121 L426.485,405.688 L425.966,404.317 L425.761,403.053 L425.89,401.939 L426.374,401.021 L427.423,400.009 L428.9,398.926 L430.676,397.836 L432.624,396.801 L434.614,395.885 L436.519,395.152 L438.209,394.666 L439.558,394.49 L441.131,394.38 L442.768,394.07 L444.404,393.59 L445.975,392.967 L447.417,392.232 L448.664,391.413 L449.654,390.539 L450.319,389.64 L450.775,388.366 L451.101,386.587 L451.298,384.454 L451.365,382.12 L451.303,379.737 L451.111,377.455 L450.789,375.427 L450.336,373.805 L449.654,372.318 L448.76,370.855 L447.696,369.46 L446.506,368.175 L445.234,367.042 L443.921,366.103 L442.611,365.401 L441.348,364.978 L440.61,364.728 L439.76,364.289 L437.809,362.937 L435.672,361.109 L433.526,358.992 L431.549,356.771 L429.918,354.633 L428.809,352.765 L428.506,351.991 L428.4,351.353 L428.605,350.03 L429.174,348.51 L430.038,346.887 L431.128,345.254 L432.376,343.706 L433.714,342.334 L435.072,341.234 L436.381,340.498 L437.553,340.141 L438.744,340.041 L439.969,340.205 L441.241,340.64 L442.576,341.351 L443.988,342.345 L445.492,343.628 L447.102,345.207 L448.199,346.156 L449.399,346.835 L450.702,347.243 L452.112,347.38 L453.628,347.247 L455.254,346.843 L456.99,346.168 L458.838,345.223 L460.605,344.076 L461.974,342.814 L462.966,341.352 L463.602,339.606 L463.903,337.49 L463.888,334.918 L463.58,331.805 L462.997,328.067 L462.285,324.449 L461.481,321.255 L460.571,318.457 L459.545,316.033 L458.391,313.958 L457.096,312.206 L455.649,310.753 L454.038,309.575 L452.388,308.422 L450.809,307.068 L449.347,305.575 L448.048,304.002 L446.958,302.411 L446.123,300.862 L445.588,299.416 L445.4,298.133 L445.602,296.83 L446.172,295.4 L447.053,293.909 L448.191,292.42 L449.531,291 L451.017,289.713 L452.594,288.624 L454.207,287.797 L455.997,287.177 L457.68,286.86 L459.255,286.844 L460.724,287.132 L462.088,287.722 L463.347,288.615 L464.502,289.811 L465.554,291.311 L467.01,293.592 L468.571,295.82 L471.822,299.901 L473.418,301.646 L474.931,303.122 L476.315,304.276 L477.523,305.053 L479.146,305.716 L480.982,306.17 L482.941,306.418 L484.935,306.461 L486.872,306.303 L488.664,305.946 L490.221,305.394 L491.454,304.647 L492.25,303.991 L492.882,303.184 L493.433,301.769 L493.989,299.286 L494.635,295.276 L495.456,289.279 L497.962,269.49 L498.864,261.726 L499.087,258.858 L499.156,256.341 L499.072,253.933 L498.832,251.389 L497.885,244.924 L496.928,238.652 L496.612,235.021 L496.694,233.84 L496.938,232.89 L497.343,232.03 L497.909,231.116 L498.924,229.89 L500.359,228.577 L502.023,227.336 L503.726,226.324 L505.902,225.379 L508.004,224.808 L510.045,224.613 L512.036,224.796 L513.989,225.36 L515.916,226.307 L517.828,227.639 L519.74,229.359 L522.035,231.789 L522.686,232.761 L523.044,233.741 L523.134,234.86 L522.985,236.244 L522.078,240.325 L521.672,242.45 L521.317,245.191 L520.761,252.143 L520.413,260.419 L520.274,269.262 L520.348,277.909 L520.637,285.602 L521.146,291.58 L521.482,293.689 L521.875,295.084 L522.778,296.998 L523.213,297.606 L523.698,298.02 L524.28,298.267 L525.007,298.377 L527.076,298.302 L528.237,298.164 L529.236,297.918 L530.148,297.5 L531.05,296.841 L532.018,295.877 L533.128,294.541 L536.079,290.49 L538.767,286.916 L540.012,285.475 L541.208,284.262 L542.366,283.275 L543.498,282.511 L544.615,281.968 L545.73,281.644 L546.853,281.536 L547.997,281.642 L549.174,281.96 L550.396,282.488 L551.673,283.224 L553.018,284.164 L555.959,286.651 L558.273,288.984 L559.127,290.062 L559.77,291.109 L560.194,292.146 L560.392,293.194 L560.358,294.274 L560.084,295.407 L559.563,296.613 L558.787,297.914 L557.751,299.331 L556.446,300.884 L553.002,304.483 L548.4,308.88 L544.655,312.468 L541.48,315.688 L539.211,318.188 L538.182,319.615 L537.831,320.343 L537.407,320.939 L536.962,321.342 L536.55,321.49 L536.11,321.673 L535.469,322.198 L533.686,324.127 L531.411,326.98 L528.853,330.463 L526.223,334.28 L523.73,338.137 L521.583,341.738 L519.994,344.787 L518.24,348.984 L517.556,351.061 L516.964,353.284 L515.942,358.636 L514.946,365.99 L511.286,394.696 L509.782,405.124 L508.408,413.417 L507.099,419.938 L505.789,425.048 L504.413,429.108 L502.904,432.481 L501.886,434.418 L500.959,435.97 L500.043,437.203 L499.056,438.188 L497.918,438.99 L496.548,439.678 L494.866,440.32 L492.791,440.984 L488.923,441.978 L487.262,442.253 L485.765,442.38 L484.42,442.36 L483.215,442.193 L482.137,441.881 L481.173,441.422 L481.172,441.422",
    "M237.233,374.707 L235.638,374.351 L234.173,373.709 L232.854,372.8 L231.695,371.641 L230.712,370.249 L229.919,368.644 L229.331,366.842 L228.964,364.861 L228.211,359.952 L227.238,354.99 L226.642,352.795 L225.809,350.321 L223.749,345.242 L222.68,342.99 L221.691,341.163 L220.861,339.937 L220.531,339.605 L220.269,339.49 L219.865,339.735 L219.417,340.45 L218.425,343.161 L217.37,347.362 L216.328,352.797 L215.819,355.266 L215.165,357.527 L214.368,359.577 L213.43,361.412 L212.352,363.029 L211.137,364.426 L209.786,365.598 L208.301,366.543 L207.632,366.774 L206.833,366.837 L205.928,366.749 L204.942,366.523 L202.82,365.718 L200.657,364.541 L198.643,363.111 L196.968,361.548 L196.318,360.753 L195.824,359.969 L195.51,359.211 L195.4,358.493 L194.995,357.268 L193.891,355.148 L192.257,352.432 L190.262,349.418 L186.515,343.898 L183.514,339.075 L180.257,333.247 L175.746,324.713 L173.573,320.327 L171.631,315.979 L170.133,312.174 L169.29,309.412 L168.494,306.656 L167.125,302.867 L165.373,298.544 L163.433,294.188 L159.657,285.811 L157.293,279.99 L156.33,277.348 L155.381,275.247 L154.364,273.619 L153.196,272.395 L151.793,271.509 L150.074,270.891 L147.955,270.473 L145.354,270.189 L141.54,269.661 L137.355,268.644 L132.504,267.052 L126.69,264.801 L120.076,262.195 L117.608,261.347 L115.467,260.747 L113.482,260.353 L111.477,260.123 L106.716,259.99 L102.104,259.919 L100.52,259.788 L99.27,259.553 L98.244,259.185 L97.332,258.656 L95.406,256.995 L93.695,255.219 L93.173,254.467 L92.842,253.703 L92.678,252.851 L92.659,251.833 L92.958,248.995 L93.418,246.314 L94.056,243.616 L94.838,240.989 L95.73,238.521 L96.696,236.3 L97.701,234.414 L98.711,232.951 L99.691,231.998 L100.809,231.413 L102.262,230.933 L103.862,230.609 L105.42,230.49 L107.348,230.665 L108.21,230.91 L109.049,231.284 L110.79,232.491 L112.84,234.428 L115.117,236.559 L117.472,238.337 L119.97,239.786 L122.677,240.927 L125.658,241.785 L128.98,242.382 L132.707,242.742 L136.906,242.887 L140.167,242.857 L143.145,242.689 L145.853,242.372 L148.302,241.895 L150.506,241.244 L152.477,240.41 L154.226,239.381 L155.767,238.144 L157.112,236.688 L158.273,235.003 L159.263,233.075 L160.094,230.894 L160.778,228.448 L161.328,225.726 L161.756,222.716 L162.075,219.406 L162.198,214.623 L161.901,209.499 L161.236,204.27 L160.258,199.176 L159.02,194.452 L157.576,190.337 L156.794,188.583 L155.98,187.069 L155.141,185.827 L154.284,184.885 L153.508,184.054 L152.955,183.153 L152.626,182.155 L152.521,181.034 L152.64,179.765 L152.983,178.321 L153.551,176.677 L154.343,174.806 L155.2,173.207 L156.237,171.771 L157.434,170.512 L158.774,169.442 L160.237,168.574 L161.805,167.921 L163.46,167.495 L165.183,167.311 L166.91,167.329 L168.909,167.476 L173.186,168.061 L176.954,168.881 L178.315,169.321 L179.15,169.75 L179.474,170.321 L179.744,171.53 L180.132,176.199 L180.345,184.421 L180.415,196.862 L180.466,206.67 L180.635,214.664 L180.96,221.137 L181.48,226.384 L182.235,230.699 L183.263,234.375 L184.605,237.708 L186.299,240.99 L188.643,245.63 L189.638,247.905 L190.338,249.765 L191.007,251.492 L191.865,253.192 L192.886,254.835 L194.046,256.388 L195.316,257.819 L196.672,259.096 L198.087,260.187 L199.535,261.06 L200.756,261.547 L202.075,261.808 L203.481,261.848 L204.962,261.676 L206.508,261.297 L208.105,260.72 L209.744,259.952 L211.413,258.999 L213.099,257.869 L214.792,256.57 L216.479,255.107 L218.15,253.488 L219.793,251.721 L221.396,249.813 L222.948,247.77 L224.437,245.6 L227.445,241.293 L228.781,239.682 L230.081,238.362 L231.403,237.281 L232.806,236.385 L234.347,235.622 L236.084,234.939 L239.013,234.031 L241.538,233.576 L242.669,233.528 L243.723,233.604 L244.709,233.807 L245.634,234.142 L246.507,234.612 L247.335,235.221 L248.128,235.972 L248.892,236.869 L250.368,239.116 L251.83,241.99 L252.612,244.153 L253.27,246.857 L253.784,249.876 L254.134,252.987 L254.302,255.965 L254.268,258.583 L254.014,260.618 L253.798,261.347 L253.52,261.845 L252.721,262.428 L251.39,262.998 L249.712,263.49 L247.872,263.839 L245.831,264.18 L243.975,264.634 L242.252,265.226 L240.613,265.981 L239.008,266.927 L237.387,268.09 L235.701,269.495 L233.9,271.168 L230.295,274.505 L227.245,277.085 L225.584,278.506 L224.167,280.032 L222.989,281.678 L222.04,283.461 L221.314,285.396 L220.805,287.5 L220.503,289.789 L220.404,292.28 L220.497,294.795 L220.793,297.164 L221.311,299.434 L222.071,301.653 L223.091,303.87 L224.392,306.133 L225.992,308.49 L227.911,310.99 L230.84,314.721 L233.537,318.358 L235.987,321.875 L238.176,325.25 L240.089,328.458 L241.71,331.475 L243.025,334.278 L244.02,336.842 L245.257,340.046 L246.862,343.581 L248.627,347.017 L250.344,349.926 L253.461,355.09 L254.61,357.349 L255.481,359.413 L256.067,361.295 L256.365,363.012 L256.369,364.577 L256.075,366.007 L255.478,367.315 L254.573,368.516 L253.354,369.626 L251.818,370.66 L249.96,371.631 L247.774,372.555 L245.255,373.447 L242.4,374.322 L241.219,374.575 L239.851,374.732 L238.466,374.78 L237.233,374.707 L237.233,374.707",
    "M401.759,331.567 L399.313,329.846 L398.391,329.035 L397.842,328.397 L397.523,326.917 L397.228,323.816 L396.99,319.547 L396.841,314.565 L396.336,302.159 L395.913,295.641 L395.438,289.99 L394.458,279.165 L393.757,269.99 L393.489,266.809 L393.13,264.061 L392.727,262.04 L392.327,261.04 L391.967,260.52 L391.672,259.807 L391.473,258.994 L391.4,258.176 L391.212,256.756 L390.681,255.182 L389.856,253.523 L388.785,251.848 L387.519,250.226 L386.105,248.727 L384.593,247.419 L383.032,246.373 L381.748,245.69 L380.478,245.142 L379.118,244.709 L377.563,244.375 L373.449,243.927 L367.296,243.654 L362.25,243.596 L357.088,243.709 L352.415,243.969 L348.838,244.355 L346.259,244.706 L344.159,244.847 L342.452,244.742 L341.05,244.355 L339.868,243.648 L338.819,242.585 L337.816,241.129 L336.773,239.244 L336.356,238.353 L336.091,237.491 L335.99,236.553 L336.07,235.434 L336.832,232.224 L338.494,227.016 L339.819,223.249 L341.105,219.998 L342.203,217.61 L342.969,216.433 L343.871,215.979 L345.201,215.827 L347.072,215.974 L349.6,216.422 L354.817,217.36 L360.255,218.085 L365.712,218.592 L370.984,218.874 L375.867,218.924 L380.158,218.736 L383.654,218.303 L385.039,217.992 L386.15,217.617 L388.023,216.712 L388.6,216.2 L388.988,215.517 L389.224,214.566 L389.346,213.248 L389.396,209.118 L389.293,205.578 L388.958,202.83 L388.341,200.626 L387.396,198.716 L385.986,196.107 L385.557,195.083 L385.4,194.433 L385.286,193.753 L384.966,192.76 L383.848,190.13 L382.319,187.124 L380.652,184.325 L376.549,178.194 L373.493,173.879 L371.445,171.329 L370.787,170.698 L370.367,170.49 L369.854,170.189 L369.142,169.37 L368.325,168.159 L367.497,166.679 L365.861,163.794 L363.76,160.57 L361.336,157.184 L358.73,153.814 L356.085,150.636 L353.542,147.827 L351.243,145.565 L349.331,144.026 L347.093,142.455 L345.217,140.971 L343.684,139.546 L342.473,138.154 L341.563,136.767 L340.933,135.36 L340.565,133.905 L340.436,132.375 L340.566,130.729 L340.964,129.13 L341.592,127.63 L342.411,126.282 L343.382,125.141 L344.466,124.259 L345.626,123.691 L346.824,123.49 L348.09,123.287 L349.855,122.733 L351.885,121.915 L353.945,120.915 L355.876,119.991 L357.691,119.343 L359.407,118.971 L361.043,118.875 L362.617,119.055 L364.147,119.513 L365.65,120.249 L367.145,121.262 L367.91,122.012 L368.726,123.117 L369.587,124.565 L370.487,126.343 L372.381,130.835 L374.356,136.49 L375.06,138.203 L376.252,140.634 L379.449,146.508 L382.642,151.831 L383.832,153.572 L384.532,154.32 L384.988,154.714 L385.602,155.542 L386.979,158.016 L388.109,159.95 L389.678,162.005 L391.58,164.086 L393.709,166.099 L395.957,167.951 L398.22,169.546 L400.39,170.793 L402.36,171.596 L404.628,172.157 L406.666,172.355 L408.771,172.192 L411.237,171.672 L412.91,171.102 L414.645,170.24 L416.42,169.112 L418.216,167.742 L420.015,166.157 L421.796,164.381 L423.54,162.441 L425.228,160.36 L426.84,158.164 L428.356,155.88 L429.757,153.531 L431.023,151.143 L432.135,148.742 L433.074,146.353 L433.82,144.001 L434.353,141.711 L434.807,140.031 L435.509,138.394 L436.412,136.854 L437.468,135.466 L438.631,134.284 L439.852,133.364 L441.086,132.76 L442.284,132.526 L443.919,132.626 L445.673,132.998 L447.516,133.627 L449.42,134.499 L451.356,135.598 L453.296,136.91 L455.21,138.419 L457.069,140.112 L459.476,142.57 L461.163,144.652 L461.733,145.6 L462.117,146.512 L462.315,147.406 L462.323,148.301 L462.141,149.217 L461.766,150.172 L461.196,151.185 L460.431,152.276 L458.304,154.767 L455.37,157.796 L452.246,161.175 L448.935,165.168 L445.833,169.278 L443.334,173.004 L441.116,176.439 L438.78,179.756 L436.603,182.577 L434.863,184.525 L433.519,185.962 L432.417,187.394 L431.673,188.655 L431.4,189.579 L431.273,190.286 L430.928,190.959 L430.416,191.519 L429.792,191.893 L429.192,192.217 L428.79,192.754 L428.597,193.646 L428.626,195.039 L428.888,197.075 L429.397,199.9 L431.202,208.49 L432.253,212.77 L433.59,217.402 L435.04,221.828 L436.433,225.49 L441.135,236.99 L441.807,239.362 L442.246,242.276 L442.455,245.613 L442.439,249.254 L442.201,253.079 L441.746,256.967 L441.078,260.801 L440.201,264.46 L437.005,275.995 L436.388,277.813 L435.524,279.804 L434.528,281.726 L433.515,283.339 L432.159,285.072 L431.577,285.624 L431.005,285.993 L430.403,286.2 L429.731,286.262 L428.015,286.036 L422.417,284.936 L420.665,284.712 L419.432,284.732 L418.583,285.016 L417.981,285.583 L417.491,286.453 L416.979,287.646 L416.568,288.89 L416.277,290.338 L416.103,291.967 L416.042,293.751 L416.237,297.687 L416.827,301.948 L417.778,306.336 L419.053,310.652 L420.618,314.698 L422.437,318.276 L423.823,320.881 L424.245,321.871 L424.4,322.47 L424.149,323.349 L423.454,324.474 L422.405,325.76 L421.09,327.122 L419.597,328.474 L418.016,329.729 L416.434,330.803 L414.941,331.61 L413.042,332.385 L411.238,332.937 L409.519,333.266 L407.871,333.372 L406.283,333.256 L404.743,332.916 L403.239,332.353 L401.759,331.567 L401.759,331.567",
]

def convert(x):
    return xy.Drawing.from_shapely(x).paths

def main():
    paths = []
    for path in PATHS:
        path = xy.parse_svg_path(path)
        path.append(path[0])
        paths.extend(path)
    polygons = [geometry.Polygon(x) for x in paths]
    lines = geometry.MultiPolygon(polygons)
    for i in range(4):
        n = 3 - i
        o = i * 10
        for j in range(-n, n + 1):
            paths += convert(lines.buffer(o + j * 0.667))
    drawing = xy.Drawing(paths).scale(1, -1).rotate_and_scale_to_fit(315, 380, step=90)
    im = drawing.render()
    im.write_to_png('frog.png')
    # xy.draw(drawing)

if __name__ == '__main__':
    main()