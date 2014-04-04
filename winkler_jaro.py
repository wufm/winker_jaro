def compare(str1, str2):
  """Return approximate string comparator measure (between 0.0 and 1.0)

  DESCRIPTION:
    As described in 'An Application of the Fellegi-Sunter Model of
    Record Linkage to the 1990 U.S. Decennial Census' by William E. Winkler
    and Yves Thibaudeau.

    Based on the 'jaro' string comparator, but modifies it according to whether
    the first few characters are the same or not.

    Implemented for Washington United for Marriage / Approve74.org
    Marriage Hero, who voted who hasn't

  """

  if (str1 == str2):
    return 1.0
  jaro_winkler_marker_char = chr(1)

  len1 = len(str1)
  len2 = len(str2)
  halflen = max(len1,len2) / 2 - 1

  ass1  = ''  # Characters assigned in str1
  ass2  = '' # Characters assigned in str2
  workstr1 = str1
  workstr2 = str2

  common1 = 0    # Number of common characters
  common2 = 0

  for i in range(len1):
    start = max(0,i-halflen)
    end   = min(i+halflen+1,len2)
    index = workstr2.find(str1[i],start,end)
    if (index > -1):    # Found common character
      common1 += 1
      ass1 = ass1 + str1[i]
      workstr2 = workstr2[:index]+jaro_winkler_marker_char+workstr2[index+1:]

  for i in range(len2):
    start = max(0,i-halflen)
    end   = min(i+halflen+1,len1)
    index = workstr1.find(str2[i],start,end)
    if (index > -1):    # Found common character
      common2 += 1
      ass2 = ass2 + str2[i]
      workstr1 = workstr1[:index]+jaro_winkler_marker_char+workstr1[index+1:]

  if (common1 != common2):
    print('Winkler: Wrong common values for strings "%s" and "%s"' % \
            (str1, str2) + ', common1: %i, common2: %i' % (common1, common2) + \
            ', common should be the same.')
    common1 = float(common1+common2) / 2.0    ##### This is just a fix #####

  if (common1 == 0):
    return 0.0

  transposition = 0
  for i in range(len(ass1)):
    if (ass1[i] != ass2[i]):
      transposition += 1
  transposition = transposition / 2.0

  minlen = min(len1,len2)
  for same in range(minlen+1):
    if (str1[:same] != str2[:same]):
      break
  same -= 1
  if (same > 4):
    same = 4

  common1 = float(common1)
  w = 1.0/3.0 * (common1 / float(len1) + common1 / float(len2) + (common1-transposition) / common1)
  wn = w + same * 0.1 * (1.0 - w)
  return wn
