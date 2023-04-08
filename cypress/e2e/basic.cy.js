describe('empty spec', () => {
  beforeEach(() => {
    cy.visit('/')
  })
  it('displays the resources text', () => {
    cy.get('h1')
    .contains('Happy Maybe Podcast');
  })
  it('shows posts', () => {
    cy.get('div.post')
    .should('be.visible')
  })
})